import json
from collections.abc import Callable
from pathlib import Path

import pytest


@pytest.fixture
def valid_task() -> dict[str, object]:
    return {
        "train": [{"input": [[0]], "output": [[0]]}],
        "test": [{"input": [[1]], "output": [[1]]}],
    }


@pytest.fixture
def write_solution() -> Callable[[Path, str, str], Path]:
    def write(root: Path, source: str, task_id: str = "abc12345") -> Path:
        root.mkdir(exist_ok=True)
        path = root / f"{task_id}.py"
        path.write_text(source, encoding="utf-8")
        return path

    return write


@pytest.fixture
def write_data() -> Callable[[Path, dict[str, object], str], Path]:
    def write(
        root: Path,
        tasks: dict[str, object],
        split: str = "training",
    ) -> Path:
        split_root = root / split
        split_root.mkdir(parents=True)
        for task_id, task in tasks.items():
            (split_root / f"{task_id}.json").write_text(json.dumps(task), encoding="utf-8")
        return root

    return write
