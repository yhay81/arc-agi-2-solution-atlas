"""Executable re-arc DSL program for ARC-AGI-2 task c3e719e8.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ZERO,
    apply,
    asobject,
    canvas,
    lbind,
    mapply,
    mostcolor,
    multiply,
    ofcolor,
    paint,
    shape,
    shift,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "c3e719e8"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = shape(grid)
    x1 = multiply(x0, x0)
    x2 = canvas(ZERO, x1)
    x3 = mostcolor(grid)
    x4 = ofcolor(grid, x3)
    x5 = lbind(multiply, x0)
    x6 = apply(x5, x4)
    x7 = asobject(grid)
    x8 = lbind(shift, x7)
    x9 = mapply(x8, x6)
    x10 = paint(x2, x9)
    return x10


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
