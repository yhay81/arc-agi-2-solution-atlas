"""Executable re-arc DSL program for ARC-AGI-2 task 007bbfb7.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ZERO,
    apply,
    canvas,
    fill,
    lbind,
    mapply,
    multiply,
    ofcolor,
    other,
    palette,
    rbind,
    shape,
    shift,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "007bbfb7"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = palette(grid)
    x1 = other(x0, ZERO)
    x2 = shape(grid)
    x3 = multiply(x2, x2)
    x4 = canvas(ZERO, x3)
    x5 = ofcolor(grid, x1)
    x6 = lbind(shift, x5)
    x7 = shape(grid)
    x8 = rbind(multiply, x7)
    x9 = apply(x8, x5)
    x10 = mapply(x6, x9)
    x11 = fill(x4, x1, x10)
    return x11


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
