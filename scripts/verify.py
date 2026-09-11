"""Discover solution modules and verify every provided pair exactly."""

import argparse
import json
import sys
from collections.abc import Callable, Iterator, Mapping
from dataclasses import dataclass
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from types import ModuleType
from typing import cast

ROOT = Path(__file__).resolve().parents[1]

type Solver = Callable[[list[list[int]]], list[list[int]]]
type TaskDocument = Mapping[str, object]


@dataclass(frozen=True, slots=True)
class PairResult:
    task_id: str
    split: str
    index: int
    expected: list[list[int]]
    actual: list[list[int]] | None
    error: str | None = None

    @property
    def passed(self) -> bool:
        return self.error is None and self.actual == self.expected


@dataclass(frozen=True, slots=True)
class CorpusResult:
    task_count: int
    pair_results: tuple[PairResult, ...]
    missing_task_ids: tuple[str, ...] = ()

    @property
    def passed_pairs(self) -> int:
        return sum(result.passed for result in self.pair_results)

    @property
    def passed(self) -> bool:
        return (
            bool(self.pair_results)
            and self.passed_pairs == len(self.pair_results)
            and not self.missing_task_ids
        )


def discover_solution_paths(root: Path) -> tuple[Path, ...]:
    """Find ``<task_id>.py`` solution modules in stable task-ID order."""
    if not root.is_dir():
        return ()
    return tuple(sorted(root.glob("????????.py")))


def task_id_from_path(path: Path) -> str:
    """Extract the eight-character ARC task ID from a solution path."""
    return path.stem


def load_provided_tasks(data_root: Path) -> dict[str, TaskDocument]:
    """Load official ARC tasks, preferring complete documents in ``corrections``."""
    tasks: dict[str, TaskDocument] = {}
    for split in ("training", "evaluation"):
        for path in sorted((data_root / split).glob("????????.json")):
            raw = json.loads(path.read_text(encoding="utf-8"))
            if not isinstance(raw, dict):
                raise ValueError(f"task data must be an object: {path}")
            if path.stem in tasks:
                raise ValueError(f"duplicate task ID in provided data: {path.stem}")
            tasks[path.stem] = cast("TaskDocument", raw)
    for path in sorted((data_root / "corrections").glob("????????.json")):
        if path.stem not in tasks:
            raise ValueError(f"correction has no upstream task: {path.stem}")
        raw = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(raw, dict):
            raise ValueError(f"corrected task data must be an object: {path}")
        tasks[path.stem] = cast("TaskDocument", raw)
    return tasks


def _load_module(path: Path) -> ModuleType:
    spec = spec_from_file_location(f"arc_solution_{task_id_from_path(path)}", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load solution module: {path}")
    module = module_from_spec(spec)
    sys.modules[spec.name] = module
    try:
        spec.loader.exec_module(module)
    except BaseException:
        sys.modules.pop(spec.name, None)
        raise
    return module


def _solver_from_module(module: ModuleType, path: Path) -> Solver:
    solve = getattr(module, "solve", None)
    if not callable(solve):
        raise TypeError(f"{path} must export callable solve(grid)")
    return cast("Solver", solve)


def _normalize_grid(value: object) -> list[list[int]]:
    """Return a validated mutable ARC grid."""
    if not isinstance(value, list) or not value:
        raise ValueError("grid must be a non-empty list of rows")
    if not all(isinstance(row, list) and row for row in value):
        raise ValueError("every grid row must be a non-empty list")

    width = len(value[0])
    result: list[list[int]] = []
    for row in value:
        if len(row) != width:
            raise ValueError("grid must be rectangular")
        if not all(type(cell) is int and 0 <= cell <= 9 for cell in row):
            raise ValueError("ARC cells must be integers from 0 through 9")
        result.append(list(row))
    return result


def _pairs(
    task: TaskDocument, task_id: str
) -> Iterator[tuple[str, int, list[list[int]], list[list[int]]]]:
    for split in ("train", "test"):
        pairs = task.get(split)
        if not isinstance(pairs, list):
            raise ValueError(f"{task_id}: {split} must be a list")
        for index, pair in enumerate(pairs):
            if not isinstance(pair, dict) or "input" not in pair or "output" not in pair:
                raise ValueError(f"{task_id}: {split}[{index}] needs input and output")
            yield split, index, _normalize_grid(pair["input"]), _normalize_grid(pair["output"])


def verify_task(solution_path: Path, task: TaskDocument) -> tuple[PairResult, ...]:
    """Run one solution against every provided train and test pair."""
    task_id = task_id_from_path(solution_path)
    module = _load_module(solution_path)
    solver = _solver_from_module(module, solution_path)
    results: list[PairResult] = []
    for split, index, input_grid, expected in _pairs(task, task_id):
        try:
            actual = _normalize_grid(solver(input_grid))
            results.append(PairResult(task_id, split, index, expected, actual))
        except Exception as exc:
            results.append(PairResult(task_id, split, index, expected, None, repr(exc)))
    return tuple(results)


def verify_corpus(solutions_root: Path, data_root: Path) -> CorpusResult:
    """Verify all discovered solutions and reject missing data or an empty corpus."""
    solution_paths = discover_solution_paths(solutions_root)
    tasks = load_provided_tasks(data_root)
    missing_data = [
        task_id_from_path(path) for path in solution_paths if task_id_from_path(path) not in tasks
    ]
    if missing_data:
        raise ValueError(f"solutions without provided task data: {', '.join(missing_data)}")
    solution_ids = {task_id_from_path(path) for path in solution_paths}
    missing_solutions = tuple(sorted(set(tasks) - solution_ids))
    pair_results = tuple(
        result
        for path in solution_paths
        for result in verify_task(path, tasks[task_id_from_path(path)])
    )
    return CorpusResult(len(solution_paths), pair_results, missing_solutions)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--solutions", type=Path, default=ROOT / "solutions")
    parser.add_argument("--data", type=Path, default=ROOT / "data")
    parser.add_argument("--expected-tasks", type=int)
    args = parser.parse_args()

    result = verify_corpus(args.solutions, args.data)
    failures = [pair for pair in result.pair_results if not pair.passed]
    print(
        f"tasks={result.task_count} pairs={len(result.pair_results)} "
        f"passed={result.passed_pairs} failed={len(failures)}"
    )
    for failure in failures:
        print(
            f"FAIL {failure.task_id} {failure.split}[{failure.index}]: "
            f"{failure.error or 'mismatch'}"
        )
    for task_id in result.missing_task_ids:
        print(f"FAIL missing solution for task {task_id}")

    count_matches = args.expected_tasks is None or result.task_count == args.expected_tasks
    if not count_matches:
        print(f"FAIL expected {args.expected_tasks} tasks, found {result.task_count}")
    return 0 if result.passed and count_matches else 1


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
