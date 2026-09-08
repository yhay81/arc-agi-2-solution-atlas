from pathlib import Path

import pytest

from arc_agi_2_atlas.verify import (
    discover_solution_paths,
    load_provided_tasks,
    task_id_from_path,
    verify_corpus,
    verify_task,
)

SOLUTIONS = Path("solutions")
DATA = Path("data/provided_tasks.json")
SOLUTION_PATHS = discover_solution_paths(SOLUTIONS)
PROVIDED_TASKS = load_provided_tasks(DATA)


@pytest.mark.parametrize("solution_path", SOLUTION_PATHS, ids=task_id_from_path)
def test_every_provided_pair_matches_exactly(solution_path: Path) -> None:
    task_id = task_id_from_path(solution_path)
    failures = [
        result
        for result in verify_task(solution_path, PROVIDED_TASKS[task_id])
        if not result.passed
    ]
    assert failures == []


def test_corpus_is_non_empty_and_every_pair_passes() -> None:
    result = verify_corpus(SOLUTIONS, DATA)
    assert result.task_count > 0
    assert result.pair_results
    assert result.passed
