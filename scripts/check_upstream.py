"""Verify that bundled ARC data matches the pinned upstream snapshot."""

import argparse
import hashlib
import json
from pathlib import Path


def check(data_root: Path, metadata_path: Path) -> list[str]:
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    digest = hashlib.sha256()
    counts: dict[str, int] = {}
    pair_count = 0
    paths = sorted(
        path
        for path in data_root.rglob("*")
        if path.is_file() and path.relative_to(data_root).parts[0] != "corrections"
    )
    for path in paths:
        relative = path.relative_to(data_root).as_posix().encode()
        file_digest = hashlib.sha256(path.read_bytes()).hexdigest().encode()
        digest.update(relative + b"\0" + file_digest + b"\n")
    for split in ("training", "evaluation"):
        task_paths = sorted((data_root / split).glob("????????.json"))
        counts[split] = len(task_paths)
        for path in task_paths:
            task = json.loads(path.read_text(encoding="utf-8"))
            pair_count += len(task["train"]) + len(task["test"])
    actual = {
        "content_sha256": digest.hexdigest(),
        "task_counts": counts,
        "pair_count": pair_count,
    }
    return [
        f"{key}: expected {metadata[key]!r}, found {value!r}"
        for key, value in actual.items()
        if value != metadata[key]
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=Path("data"))
    parser.add_argument("--metadata", type=Path, default=Path("metadata/upstream.json"))
    args = parser.parse_args()
    failures = check(args.data, args.metadata)
    if failures:
        for failure in failures:
            print(f"FAIL {failure}")
        return 1
    metadata = json.loads(args.metadata.read_text(encoding="utf-8"))
    print(
        f"upstream={metadata['commit']} tasks={sum(metadata['task_counts'].values())} "
        f"pairs={metadata['pair_count']} digest={metadata['content_sha256']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
