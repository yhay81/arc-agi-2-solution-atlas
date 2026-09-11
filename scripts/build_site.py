"""Build the static ARC-AGI-2 task viewer."""

import json
import shutil
from dataclasses import dataclass
from pathlib import Path

from scripts.verify import load_provided_tasks

ROOT = Path(__file__).resolve().parents[1]
SITE_SOURCE = ROOT / "site"
OUTPUT = ROOT / ".site-build"


@dataclass(frozen=True, slots=True)
class SolutionMetadata:
    documentation: str
    concepts: tuple[str, ...]
    program: str


def read_solution(path: Path) -> SolutionMetadata:
    """Read public documentation and concepts without executing a solver."""
    program = path.read_text(encoding="utf-8")
    note_path = ROOT / "notes" / f"{path.stem}.json"
    note = json.loads(note_path.read_text(encoding="utf-8"))
    sections = [note["title"]]
    steps = "\n".join(f"{index}. {step}" for index, step in enumerate(note["steps"], 1))
    sections.append(f"Transformation steps\n{steps}")
    parameters = note.get("parameters", ())
    if parameters:
        sections.append("Rule parameters\n" + "\n".join(f"- {item}" for item in parameters))
    documentation = "\n\n".join(sections)
    concepts = tuple(note["concepts"])
    return SolutionMetadata(documentation, concepts, program)


def build() -> None:
    """Copy site assets and generate its compact task catalog."""
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    shutil.copytree(SITE_SOURCE, OUTPUT)

    tasks: list[dict[str, object]] = []
    pair_count = 0
    reviewed_tasks = load_provided_tasks(ROOT / "data")
    for split in ("training", "evaluation"):
        for task_path in sorted((ROOT / "data" / split).glob("????????.json")):
            solution_path = ROOT / "solutions" / f"{task_path.stem}.py"
            task = reviewed_tasks[task_path.stem]
            train, test = task["train"], task["test"]
            if not isinstance(train, list) or not isinstance(test, list):
                raise ValueError(f"invalid task document: {task_path.stem}")
            metadata = read_solution(solution_path)
            pair_count += len(train) + len(test)
            tasks.append(
                {
                    "id": task_path.stem,
                    "split": split,
                    "documentation": metadata.documentation,
                    "concepts": metadata.concepts,
                    "program": metadata.program,
                    "task": task,
                }
            )
    catalog = {"pair_count": pair_count, "tasks": tasks}
    (OUTPUT / "catalog.json").write_text(
        json.dumps(catalog, ensure_ascii=False, separators=(",", ":")), encoding="utf-8"
    )


if __name__ == "__main__":
    build()
