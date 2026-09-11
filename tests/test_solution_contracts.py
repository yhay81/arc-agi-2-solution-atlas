import ast
import hashlib
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any, cast

FORBIDDEN_SOURCE_MARKERS = {
    "ArunSehrawat/arc-agi2-solutions",
    "arcprize/ARC-TGI",
    "michaelhodel/re-arc",
    "thebowenfeng/arc-abstractions",
}

NEIGHBORHOOD_WIDTHS = {5, 9}
# This task asks the solver to restore crops of a random canvas revealed by its
# training outputs. With the solve(grid) interface, retaining that learned
# canvas is necessary rather than an input-replay shortcut.
TRAINING_DERIVED_BINARY_TEMPLATES = {"269e22fb"}


def _is_numeric_neighborhood(node: ast.AST) -> bool:
    return (
        isinstance(node, (ast.List, ast.Tuple))
        and len(node.elts) in NEIGHBORHOOD_WIDTHS
        and all(
            isinstance(item, ast.Constant) and isinstance(item.value, int) for item in node.elts
        )
    )


def _fixed_neighborhood_entries(node: ast.AST) -> int:
    if isinstance(node, ast.Dict):
        return sum(key is not None and _is_numeric_neighborhood(key) for key in node.keys)
    if isinstance(node, (ast.List, ast.Tuple)):
        return sum(
            isinstance(entry, (ast.List, ast.Tuple))
            and len(entry.elts) == 2
            and _is_numeric_neighborhood(entry.elts[0])
            for entry in node.elts
        )
    return 0


def solution_violations(root: Path) -> list[str]:
    failures: list[str] = []
    for path in sorted(root.glob("????????.py")):
        source = path.read_text(encoding="utf-8")
        module = ast.parse(source, filename=str(path))
        imports = {
            node.module
            for node in ast.walk(module)
            if isinstance(node, ast.ImportFrom) and node.module is not None
        } | {
            alias.name
            for node in ast.walk(module)
            if isinstance(node, ast.Import)
            for alias in node.names
        }
        problems = [
            f"non-standard-library import {name}"
            for name in sorted(imports)
            if name != "__future__" and name.split(".", 1)[0] not in sys.stdlib_module_names
        ]
        solvers = [
            node
            for node in module.body
            if isinstance(node, ast.FunctionDef) and node.name == "solve"
        ]
        if len(solvers) != 1:
            problems.append(f"expected exactly one top-level solve(grid), found {len(solvers)}")
        else:
            arguments = solvers[0].args
            if not (
                len(arguments.args) == 1
                and arguments.args[0].arg == "grid"
                and arguments.args[0].annotation is None
                and not arguments.posonlyargs
                and not arguments.defaults
                and not arguments.kwonlyargs
                and arguments.vararg is None
                and arguments.kwarg is None
                and solvers[0].returns is None
            ):
                problems.append("public solver must have signature def solve(grid)")
        if any(isinstance(node, ast.Assert) for node in ast.walk(module)):
            problems.append("assert statement; raise an explicit exception instead")
        markers = sorted(marker for marker in FORBIDDEN_SOURCE_MARKERS if marker in source)
        if markers:
            problems.append(f"external source marker {', '.join(markers)}")
        if "hashlib" in imports:
            problems.append("input-replay import hashlib")
        if any(
            isinstance(target, ast.Name) and target.id == "TASKS"
            for node in module.body
            if isinstance(node, ast.Assign)
            for target in node.targets
        ):
            problems.append("embedded task data")
        literal_items = sum(
            len(node.elts)
            for node in ast.walk(module)
            if isinstance(node, (ast.List, ast.Set, ast.Tuple))
        )
        if literal_items > 499:
            problems.append(f"oversized literal table ({literal_items} items)")
        neighborhood_entries = max(
            (_fixed_neighborhood_entries(node) for node in ast.walk(module)), default=0
        )
        if neighborhood_entries >= 10:
            problems.append(f"fixed neighborhood lookup table ({neighborhood_entries} entries)")
        binary_template_size = sum(
            len(node.value)
            for node in ast.walk(module)
            if isinstance(node, ast.Constant)
            and isinstance(node.value, str)
            and node.value
            and set(node.value) <= {"0", "1"}
        )
        if binary_template_size > 255 and path.stem not in TRAINING_DERIVED_BINARY_TEMPLATES:
            problems.append(f"embedded binary template ({binary_template_size} cells)")
        if problems:
            failures.append(f"{path}: {'; '.join(problems)}")
    return failures


def _read_solution(path: Path) -> Any:
    spec = importlib.util.spec_from_file_location("atlas_build_site", "scripts/build_site.py")
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return cast("Any", module).read_solution(path)


def test_solution_displays_its_transformation() -> None:
    metadata = _read_solution(Path("solutions/1cf80156.py"))
    concise_metadata = _read_solution(Path("solutions/00576224.py"))

    assert "def solve" in metadata.program
    assert "Transformation steps" in metadata.documentation
    assert "Evidence and limitations" not in metadata.documentation
    assert "Training-pair observations" not in metadata.documentation
    assert "Rule parameters" not in concise_metadata.documentation
    assert concise_metadata.documentation.count("Tile the input into a 3-by-3") == 1
    assert "This is the training-inferred" not in concise_metadata.documentation


def test_solution_signature_must_be_solve_grid(tmp_path: Path) -> None:
    (tmp_path / "abc12345.py").write_text("def solve(grid): return grid\n", encoding="utf-8")
    assert solution_violations(tmp_path) == []

    (tmp_path / "abc12345.py").write_text(
        "def solve(grid: list[list[int]]) -> list[list[int]]: return grid\n",
        encoding="utf-8",
    )
    assert "public solver must have signature def solve(grid)" in solution_violations(tmp_path)[0]


def test_solution_signature_rejects_alias(tmp_path: Path) -> None:
    (tmp_path / "abc12345.py").write_text(
        "def solve_abc12345(grid): return grid\nsolve = solve_abc12345\n",
        encoding="utf-8",
    )
    assert "expected exactly one top-level solve(grid), found 0" in solution_violations(tmp_path)[0]


def test_solution_rejects_fixed_neighborhood_lookup_table(tmp_path: Path) -> None:
    entries = ",\n".join(f"({index}, 0, 0, 0, 0): {index}" for index in range(10))
    (tmp_path / "abc12345.py").write_text(
        f"def solve(grid):\n    labels = {{{entries}}}\n    return grid\n",
        encoding="utf-8",
    )

    assert "fixed neighborhood lookup table (10 entries)" in solution_violations(tmp_path)[0]


def test_solution_rejects_unregistered_binary_template(tmp_path: Path) -> None:
    rows = repr(tuple("01" * 16 for _ in range(16)))
    (tmp_path / "abc12345.py").write_text(
        f"def solve(grid):\n    template = {rows}\n    return grid\n",
        encoding="utf-8",
    )

    assert "embedded binary template (512 cells)" in solution_violations(tmp_path)[0]


def test_all_solutions_satisfy_architecture_contract() -> None:
    assert solution_violations(Path("solutions")) == []


def test_solution_manifest_is_current() -> None:
    paths = sorted(Path("solutions").glob("????????.py"))
    manifest = {path.stem: hashlib.sha256(path.read_bytes()).hexdigest() for path in paths}
    metadata = json.loads(Path("metadata/solutions.json").read_text(encoding="utf-8"))
    task_ids = {
        path.stem
        for split in ("training", "evaluation")
        for path in (Path("data") / split).glob("????????.json")
    }

    assert metadata.get("solution_sha256") == manifest
    assert metadata.get("total_solution_count") == len(manifest)
    assert metadata.get("unsolved_task_ids") == sorted(task_ids - set(manifest))
