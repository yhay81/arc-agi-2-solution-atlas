"""Executable re-arc DSL program for ARC-AGI-2 task be94b721.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    F,
    T,
    argmax,
    canvas,
    color,
    normalize,
    objects,
    paint,
    remove,
    shape,
    size,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "be94b721"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, F)
    x1 = argmax(x0, size)
    x2 = color(x1)
    x3 = remove(x1, x0)
    x4 = argmax(x3, size)
    x5 = shape(x4)
    x6 = canvas(x2, x5)
    x7 = normalize(x4)
    x8 = paint(x6, x7)
    return x8


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
