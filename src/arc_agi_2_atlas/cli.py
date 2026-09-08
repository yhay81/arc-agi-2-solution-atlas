"""Command-line interface for corpus verification."""

import argparse
from pathlib import Path

from arc_agi_2_atlas.verify import verify_corpus


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["verify"])
    parser.add_argument("--solutions", type=Path, default=Path("solutions"))
    parser.add_argument("--expected-tasks", type=int)
    args = parser.parse_args()

    result = verify_corpus(args.solutions)
    failures = [pair for pair in result.pair_results if not pair.passed]
    print(
        f"tasks={result.task_count} pairs={len(result.pair_results)} "
        f"passed={result.passed_pairs} failed={len(failures)}"
    )
    for failure in failures:
        print(
            f"FAIL {failure.task_id} {failure.split}[{failure.index}]: {failure.error or 'mismatch'}"
        )

    count_matches = args.expected_tasks is None or result.task_count == args.expected_tasks
    if not count_matches:
        print(f"FAIL expected {args.expected_tasks} tasks, found {result.task_count}")
    return 0 if result.passed and count_matches else 1


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
