"""Discover solution packages and verify every provided pair exactly."""

import json
from collections.abc import Callable, Iterator
from dataclasses import dataclass
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from types import ModuleType
from typing import cast

from arc_agi_2_atlas.types import Grid, normalize_grid

Solver = Callable[[Grid], Grid]


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


def discover_task_directories(root: Path) -> tuple[Path, ...]:
    """Find complete solution packages in stable task-id order."""
    if not root.is_dir():
        return ()
    return tuple(
        directory
        for directory in sorted(root.iterdir())
        if directory.is_dir()
        and (directory / "task.json").is_file()
        and (directory / "solution.py").is_file()
    )


def _load_solver(path: Path) -> Solver:
    spec = spec_from_file_location(f"arc_solution_{path.parent.name}", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load solver module: {path}")
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return _solver_from_module(module, path)


def _solver_from_module(module: ModuleType, path: Path) -> Solver:
    solve = getattr(module, "solve", None)
    if not callable(solve):
        raise TypeError(f"{path} must export callable solve(grid)")
    return cast("Solver", solve)


def _pairs(task_path: Path) -> Iterator[tuple[str, int, Grid, Grid]]:
    raw = json.loads(task_path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise ValueError(f"task must be an object: {task_path}")
    for split in ("train", "test"):
        pairs = raw.get(split)
        if not isinstance(pairs, list):
            raise ValueError(f"{task_path}: {split} must be a list")
        for index, pair in enumerate(pairs):
            if not isinstance(pair, dict) or "input" not in pair or "output" not in pair:
                raise ValueError(f"{task_path}: {split}[{index}] needs input and output")
            yield split, index, normalize_grid(pair["input"]), normalize_grid(pair["output"])


def verify_task(task_directory: Path) -> tuple[PairResult, ...]:
    """Run one task's solver against every provided train and test pair."""
    task_id = task_directory.name
    solver = _load_solver(task_directory / "solution.py")
    results: list[PairResult] = []
    for split, index, input_grid, expected in _pairs(task_directory / "task.json"):
        try:
            actual = normalize_grid(solver(input_grid))
            results.append(PairResult(task_id, split, index, expected, actual))
        except Exception as exc:
            results.append(PairResult(task_id, split, index, expected, None, repr(exc)))
    return tuple(results)


def verify_corpus(solutions_root: Path) -> CorpusResult:
    """Verify all discovered tasks and reject an empty corpus."""
    task_directories = discover_task_directories(solutions_root)
    pair_results = tuple(
        result for directory in task_directories for result in verify_task(directory)
    )
    return CorpusResult(len(task_directories), pair_results)
