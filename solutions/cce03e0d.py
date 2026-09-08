"""Executable re-arc DSL program for ARC-AGI-2 task cce03e0d.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    TWO,
    ZERO,
    apply,
    asobject,
    canvas,
    lbind,
    mapply,
    multiply,
    ofcolor,
    paint,
    rbind,
    shape,
    shift,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "cce03e0d"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = ofcolor(grid, TWO)
    x1 = shape(grid)
    x2 = multiply(x1, x1)
    x3 = canvas(ZERO, x2)
    x4 = rbind(multiply, x1)
    x5 = apply(x4, x0)
    x6 = asobject(grid)
    x7 = lbind(shift, x6)
    x8 = mapply(x7, x5)
    x9 = paint(x3, x8)
    return x9


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
