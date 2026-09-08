"""Build the static ARC-AGI-2 task viewer."""

import ast
import json
import shutil
from dataclasses import dataclass
from pathlib import Path

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
    module = ast.parse(program, filename=str(path))
    documentation = ast.get_docstring(module, clean=False) or "No documentation yet."
    concepts: tuple[str, ...] = ()
    for node in module.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == "CONCEPTS" for target in node.targets
        ):
            value = ast.literal_eval(node.value)
            if isinstance(value, tuple) and all(isinstance(item, str) for item in value):
                concepts = value
    return SolutionMetadata(documentation, concepts, program)


def build() -> None:
    """Copy site assets and generate its compact task catalog."""
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    shutil.copytree(SITE_SOURCE, OUTPUT)

    tasks: list[dict[str, object]] = []
    pair_count = 0
    for split in ("training", "evaluation"):
        for task_path in sorted((ROOT / "data" / split).glob("????????.json")):
            solution_path = ROOT / "solutions" / f"{task_path.stem}.py"
            if not solution_path.exists():
                continue
            task = json.loads(task_path.read_text(encoding="utf-8"))
            metadata = read_solution(solution_path)
            pair_count += len(task["train"]) + len(task["test"])
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
