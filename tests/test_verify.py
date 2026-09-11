import json
import sys
from pathlib import Path
from typing import Protocol, cast

import pytest

from scripts.verify import (
    ROOT,
    TaskDocument,
    _normalize_grid,
    discover_solution_paths,
    load_provided_tasks,
    main,
    task_id_from_path,
    verify_corpus,
    verify_task,
)


class WriteSolution(Protocol):
    def __call__(self, root: Path, source: str, task_id: str = "abc12345") -> Path: ...


class WriteData(Protocol):
    def __call__(
        self,
        root: Path,
        tasks: dict[str, object],
        split: str = "training",
    ) -> Path: ...


# Grid validation


@pytest.mark.parametrize(
    "value",
    [[], [[0], []], [[0], [0, 1]], [[-1]], [[10]], [[True]], "not a grid"],
)
def test_normalize_grid_rejects_invalid_grids(value: object) -> None:
    with pytest.raises(ValueError):
        _normalize_grid(value)


def test_normalize_grid_copies_valid_grid() -> None:
    source = [[0, 1], [2, 3]]
    result = _normalize_grid(source)
    assert result == source
    assert result is not source


# Task discovery and loading


def test_discovery_uses_task_id_modules_only(
    tmp_path: Path,
    write_solution: WriteSolution,
) -> None:
    assert discover_solution_paths(tmp_path / "missing") == ()
    write_solution(tmp_path, "", "abc12345")
    (tmp_path / "notes.py").write_text("", encoding="utf-8")
    paths = discover_solution_paths(tmp_path)
    assert [task_id_from_path(path) for path in paths] == ["abc12345"]


@pytest.mark.parametrize("data", [[], "invalid"])
def test_invalid_provided_data_is_rejected(
    tmp_path: Path,
    data: object,
    write_data: WriteData,
) -> None:
    path = write_data(tmp_path / "data", {"abc12345": data})
    with pytest.raises(ValueError):
        load_provided_tasks(path)


def test_corrected_task_document_overrides_upstream_copy(
    tmp_path: Path,
    valid_task: dict[str, object],
    write_data: WriteData,
) -> None:
    data = write_data(tmp_path / "data", {"abc12345": valid_task})
    corrected = json.loads(json.dumps(valid_task))
    corrected["test"][0]["output"] = [[2]]
    write_data(data, {"abc12345": corrected}, "corrections")
    tasks = cast("dict[str, dict[str, list[dict[str, object]]]]", load_provided_tasks(data))
    assert tasks["abc12345"]["test"][0]["output"] == [[2]]
    assert json.loads((data / "training" / "abc12345.json").read_text())["test"][0]["output"] == [
        [1]
    ]


def test_correction_without_upstream_task_is_rejected(
    tmp_path: Path,
    valid_task: dict[str, object],
    write_data: WriteData,
) -> None:
    data = write_data(tmp_path / "data", {})
    write_data(data, {"abc12345": valid_task}, "corrections")
    with pytest.raises(ValueError, match="no upstream task"):
        load_provided_tasks(data)


def test_invalid_corrected_document_is_rejected(
    tmp_path: Path,
    valid_task: dict[str, object],
    write_data: WriteData,
) -> None:
    data = write_data(tmp_path / "data", {"abc12345": valid_task})
    write_data(data, {"abc12345": []}, "corrections")
    with pytest.raises(ValueError, match="corrected task data must be an object"):
        load_provided_tasks(data)


# Solver loading and execution


def test_solver_must_export_solve(
    tmp_path: Path,
    valid_task: dict[str, object],
    write_solution: WriteSolution,
) -> None:
    path = write_solution(tmp_path, "value = 1\n")
    with pytest.raises(TypeError, match="must export callable"):
        verify_task(path, cast("TaskDocument", valid_task))


def test_solution_module_supports_dataclasses(
    tmp_path: Path,
    valid_task: dict[str, object],
    write_solution: WriteSolution,
) -> None:
    path = write_solution(
        tmp_path,
        "from dataclasses import dataclass\n"
        "@dataclass\nclass Cell:\n    value: int\n"
        "def solve(grid): return [[Cell(grid[0][0]).value]]\n",
    )
    assert all(result.passed for result in verify_task(path, cast("TaskDocument", valid_task)))


def test_solution_import_errors_are_propagated_and_cleaned_up(
    tmp_path: Path,
    valid_task: dict[str, object],
    write_solution: WriteSolution,
) -> None:
    path = write_solution(tmp_path, 'raise RuntimeError("import failed")\n')
    with pytest.raises(RuntimeError, match="import failed"):
        verify_task(path, cast("TaskDocument", valid_task))
    assert "arc_solution_abc12345" not in sys.modules


@pytest.mark.parametrize(
    "task",
    [{}, {"train": {}, "test": []}, {"train": [{}], "test": []}],
)
def test_invalid_task_documents_are_rejected(
    tmp_path: Path,
    task: object,
    write_solution: WriteSolution,
) -> None:
    path = write_solution(tmp_path, "def solve(grid): return grid\n")
    with pytest.raises(ValueError):
        verify_task(path, cast("TaskDocument", task))


def test_solver_exceptions_are_reported_per_pair(
    tmp_path: Path,
    valid_task: dict[str, object],
    write_solution: WriteSolution,
) -> None:
    path = write_solution(tmp_path, 'def solve(grid): raise RuntimeError("broken")\n')
    results = verify_task(path, cast("TaskDocument", valid_task))
    assert len(results) == 2
    assert all(not result.passed for result in results)
    assert all(result.actual is None for result in results)
    assert all("broken" in (result.error or "") for result in results)


# Corpus verification


def test_corpus_rejects_solution_without_data(
    tmp_path: Path,
    write_solution: WriteSolution,
    write_data: WriteData,
) -> None:
    solutions = tmp_path / "solutions"
    write_solution(solutions, "def solve(grid): return grid\n")
    data = write_data(tmp_path / "data", {})
    with pytest.raises(ValueError, match="without provided task data"):
        verify_corpus(solutions, data)


def test_empty_corpus_fails(
    tmp_path: Path,
    write_data: WriteData,
) -> None:
    data = write_data(tmp_path / "data", {})
    result = verify_corpus(tmp_path / "solutions", data)
    assert result.task_count == 0
    assert result.pair_results == ()
    assert result.passed_pairs == 0
    assert not result.passed


def test_corpus_reports_data_without_solution(
    tmp_path: Path,
    valid_task: dict[str, object],
    write_solution: WriteSolution,
    write_data: WriteData,
) -> None:
    solutions = tmp_path / "solutions"
    write_solution(solutions, "def solve(grid): return grid\n")
    data = write_data(
        tmp_path / "data",
        {"abc12345": valid_task, "def67890": valid_task},
    )
    result = verify_corpus(solutions, data)
    assert result.missing_task_ids == ("def67890",)
    assert not result.passed


# Command-line interface


def test_cli_reports_pair_failure(monkeypatch, capsys, tmp_path: Path) -> None:
    solutions = tmp_path / "solutions"
    training = tmp_path / "data" / "training"
    solutions.mkdir()
    training.mkdir(parents=True)
    (solutions / "abc12345.py").write_text("def solve(grid): return [[1]]\n", encoding="utf-8")
    task = {"train": [{"input": [[0]], "output": [[0]]}], "test": []}
    (training / "abc12345.json").write_text(json.dumps(task), encoding="utf-8")
    monkeypatch.setattr(
        sys,
        "argv",
        ["verify.py", "--solutions", str(solutions), "--data", str(training.parent)],
    )
    assert main() == 1
    assert "FAIL abc12345 train[0]: mismatch" in capsys.readouterr().out


def test_cli_rejects_wrong_task_count(monkeypatch, capsys, tmp_path: Path) -> None:
    monkeypatch.setattr(
        sys,
        "argv",
        ["verify.py", "--solutions", str(tmp_path), "--expected-tasks", "1120"],
    )
    assert main() == 1
    output = capsys.readouterr().out
    assert "expected 1120 tasks, found 0" in output


def test_cli_defaults_to_checkout_corpus(monkeypatch, tmp_path: Path) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(sys, "argv", ["verify.py", "--solutions", str(tmp_path)])
    assert main() == 1
    assert (ROOT / "data").is_dir()
