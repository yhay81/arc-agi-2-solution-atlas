"""Discover solution modules and verify every provided pair exactly."""

import json
from collections.abc import Callable, Iterator, Mapping
from dataclasses import dataclass
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from types import ModuleType
from typing import cast

from arc_agi_2_atlas.types import Grid, normalize_grid

type Solver = Callable[[Grid], Grid]
type TaskDocument = Mapping[str, object]


@dataclass(frozen=True, slots=True)
class PairResult:
    task_id: str
    split: str
    index: int
    expected: Grid
    actual: Grid | None
    error: str | None = None

    @property
    def passed(self) -> bool:
        return self.error is None and self.actual == self.expected


@dataclass(frozen=True, slots=True)
class CorpusResult:
    task_count: int
    pair_results: tuple[PairResult, ...]

    @property
    def passed_pairs(self) -> int:
        return sum(result.passed for result in self.pair_results)

    @property
    def passed(self) -> bool:
        return bool(self.pair_results) and self.passed_pairs == len(self.pair_results)


def discover_solution_paths(root: Path) -> tuple[Path, ...]:
    """Find ``task_<id>.py`` solution modules in stable task-ID order."""
    if not root.is_dir():
        return ()
    return tuple(sorted(root.glob("task_????????.py")))


def task_id_from_path(path: Path) -> str:
    """Extract the eight-character ARC task ID from a solution path."""
    return path.stem.removeprefix("task_")


def load_provided_tasks(path: Path) -> dict[str, TaskDocument]:
    """Load the shared mapping of task IDs to provided input/output pairs."""
    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise ValueError(f"provided task data must be an object: {path}")
    valid = all(
        isinstance(task_id, str) and isinstance(task, dict) for task_id, task in raw.items()
    )
    if not valid:
        raise ValueError(f"provided task data contains an invalid entry: {path}")
    return cast("dict[str, TaskDocument]", raw)


def _load_module(path: Path) -> ModuleType:
    spec = spec_from_file_location(f"arc_solution_{task_id_from_path(path)}", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load solution module: {path}")
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _solver_from_module(module: ModuleType, path: Path) -> Solver:
    solve = getattr(module, "solve", None)
    if not callable(solve):
        raise TypeError(f"{path} must export callable solve(grid)")
    return cast("Solver", solve)


def _pairs(task: TaskDocument, task_id: str) -> Iterator[tuple[str, int, Grid, Grid]]:
    for split in ("train", "test"):
        pairs = task.get(split)
        if not isinstance(pairs, list):
            raise ValueError(f"{task_id}: {split} must be a list")
        for index, pair in enumerate(pairs):
            if not isinstance(pair, dict) or "input" not in pair or "output" not in pair:
                raise ValueError(f"{task_id}: {split}[{index}] needs input and output")
            yield split, index, normalize_grid(pair["input"]), normalize_grid(pair["output"])


def verify_task(solution_path: Path, task: TaskDocument) -> tuple[PairResult, ...]:
    """Run one solution against every provided train and test pair."""
    task_id = task_id_from_path(solution_path)
    module = _load_module(solution_path)
    if getattr(module, "TASK_ID", None) != task_id:
        raise ValueError(f"{solution_path}: TASK_ID must equal {task_id!r}")
    solver = _solver_from_module(module, solution_path)
    results: list[PairResult] = []
    for split, index, input_grid, expected in _pairs(task, task_id):
        try:
            actual = normalize_grid(solver(input_grid))
            results.append(PairResult(task_id, split, index, expected, actual))
        except Exception as exc:
            results.append(PairResult(task_id, split, index, expected, None, repr(exc)))
    return tuple(results)


def verify_corpus(solutions_root: Path, data_path: Path) -> CorpusResult:
    """Verify all discovered solutions and reject missing data or an empty corpus."""
    solution_paths = discover_solution_paths(solutions_root)
    tasks = load_provided_tasks(data_path)
    missing_data = [
        task_id_from_path(path) for path in solution_paths if task_id_from_path(path) not in tasks
    ]
    if missing_data:
        raise ValueError(f"solutions without provided task data: {', '.join(missing_data)}")
    pair_results = tuple(
        result
        for path in solution_paths
        for result in verify_task(path, tasks[task_id_from_path(path)])
    )
    return CorpusResult(len(solution_paths), pair_results)
