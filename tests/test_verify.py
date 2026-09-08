import json
from pathlib import Path
from typing import cast

import pytest

from arc_agi_2_atlas.verify import (
    TaskDocument,
    discover_solution_paths,
    load_provided_tasks,
    task_id_from_path,
    verify_corpus,
    verify_task,
)

VALID_TASK = {
    "train": [{"input": [[0]], "output": [[0]]}],
    "test": [{"input": [[1]], "output": [[1]]}],
}


def _write_solution(root: Path, source: str, task_id: str = "abc12345") -> Path:
    root.mkdir(exist_ok=True)
    path = root / f"{task_id}.py"
    path.write_text(source, encoding="utf-8")
    return path


def _write_data(root: Path, tasks: dict[str, object], split: str = "training") -> Path:
    split_root = root / split
    split_root.mkdir(parents=True)
    for task_id, task in tasks.items():
        (split_root / f"{task_id}.json").write_text(json.dumps(task), encoding="utf-8")
    return root


def test_discovery_uses_task_id_modules_only(tmp_path: Path) -> None:
    assert discover_solution_paths(tmp_path / "missing") == ()
    _write_solution(tmp_path, "", "abc12345")
    (tmp_path / "notes.py").write_text("", encoding="utf-8")
    paths = discover_solution_paths(tmp_path)
    assert [task_id_from_path(path) for path in paths] == ["abc12345"]


@pytest.mark.parametrize("data", [[], "invalid"])
def test_invalid_provided_data_is_rejected(tmp_path: Path, data: object) -> None:
    path = _write_data(tmp_path / "data", {"abc12345": data})
    with pytest.raises(ValueError):
        load_provided_tasks(path)


def test_solver_must_export_solve(tmp_path: Path) -> None:
    path = _write_solution(tmp_path, 'TASK_ID = "abc12345"\n')
    with pytest.raises(TypeError, match="must export callable"):
        verify_task(path, VALID_TASK)


def test_declared_task_id_must_match_filename(tmp_path: Path) -> None:
    path = _write_solution(tmp_path, 'TASK_ID = "wrong"\ndef solve(grid): return grid\n')
    with pytest.raises(ValueError, match="TASK_ID"):
        verify_task(path, VALID_TASK)


@pytest.mark.parametrize(
    "task",
    [{}, {"train": {}, "test": []}, {"train": [{}], "test": []}],
)
def test_invalid_task_documents_are_rejected(tmp_path: Path, task: object) -> None:
    path = _write_solution(
        tmp_path,
        'TASK_ID = "abc12345"\ndef solve(grid): return grid\n',
    )
    with pytest.raises(ValueError):
        verify_task(path, cast("TaskDocument", task))


def test_solver_exceptions_are_reported_per_pair(tmp_path: Path) -> None:
    path = _write_solution(
        tmp_path,
        'TASK_ID = "abc12345"\ndef solve(grid): raise RuntimeError("broken")\n',
    )
    results = verify_task(path, VALID_TASK)
    assert len(results) == 2
    assert all(not result.passed for result in results)
    assert all(result.actual is None for result in results)
    assert all("broken" in (result.error or "") for result in results)


def test_corpus_rejects_solution_without_data(tmp_path: Path) -> None:
    solutions = tmp_path / "solutions"
    _write_solution(solutions, 'TASK_ID = "abc12345"\ndef solve(grid): return grid\n')
    data = _write_data(tmp_path / "data", {})
    with pytest.raises(ValueError, match="without provided task data"):
        verify_corpus(solutions, data)


def test_empty_corpus_fails(tmp_path: Path) -> None:
    data = _write_data(tmp_path / "data", {})
    result = verify_corpus(tmp_path / "solutions", data)
    assert result.task_count == 0
    assert result.pair_results == ()
    assert result.passed_pairs == 0
    assert not result.passed
