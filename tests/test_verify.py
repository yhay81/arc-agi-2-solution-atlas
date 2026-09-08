import json
from pathlib import Path

import pytest

from arc_agi_2_atlas.verify import discover_task_directories, verify_corpus, verify_task


def _write_package(root: Path, task: object, solution: str) -> Path:
    package = root / "abc12345"
    package.mkdir()
    (package / "task.json").write_text(json.dumps(task), encoding="utf-8")
    (package / "solution.py").write_text(solution, encoding="utf-8")
    return package


def test_discovery_rejects_missing_root_and_incomplete_packages(tmp_path: Path) -> None:
    assert discover_task_directories(tmp_path / "missing") == ()
    (tmp_path / "incomplete").mkdir()
    assert discover_task_directories(tmp_path) == ()


def test_solver_must_export_solve(tmp_path: Path) -> None:
    package = _write_package(
        tmp_path,
        {"train": [], "test": []},
        "value = 1\n",
    )
    with pytest.raises(TypeError, match="must export callable"):
        verify_task(package)


@pytest.mark.parametrize(
    "task",
    [
        [],
        {},
        {"train": {}, "test": []},
        {"train": [{}], "test": []},
    ],
)
def test_invalid_task_documents_are_rejected(tmp_path: Path, task: object) -> None:
    package = _write_package(tmp_path, task, "def solve(grid): return grid\n")
    with pytest.raises(ValueError):
        verify_task(package)


def test_solver_exceptions_are_reported_per_pair(tmp_path: Path) -> None:
    package = _write_package(
        tmp_path,
        {
            "train": [{"input": [[0]], "output": [[1]]}],
            "test": [{"input": [[2]], "output": [[2]]}],
        },
        "def solve(grid):\n    raise RuntimeError('broken')\n",
    )
    results = verify_task(package)
    assert len(results) == 2
    assert all(not result.passed for result in results)
    assert all(result.actual is None for result in results)
    assert all("broken" in (result.error or "") for result in results)


def test_empty_corpus_fails(tmp_path: Path) -> None:
    result = verify_corpus(tmp_path)
    assert result.task_count == 0
    assert result.pair_results == ()
    assert result.passed_pairs == 0
    assert not result.passed
