from pathlib import Path

import pytest

from arc_agi_2_atlas.verify import discover_task_directories, verify_corpus, verify_task

SOLUTIONS = Path("solutions")
TASK_DIRECTORIES = discover_task_directories(SOLUTIONS)


@pytest.mark.parametrize("task_directory", TASK_DIRECTORIES, ids=lambda path: path.name)
def test_every_provided_pair_matches_exactly(task_directory: Path) -> None:
    failures = [result for result in verify_task(task_directory) if not result.passed]
    assert failures == []


def test_corpus_is_non_empty_and_every_pair_passes() -> None:
    result = verify_corpus(SOLUTIONS)
    assert result.task_count > 0
    assert result.pair_results
    assert result.passed
