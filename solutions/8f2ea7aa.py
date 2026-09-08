"""Executable re-arc DSL program for ARC-AGI-2 task 8f2ea7aa.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.re_arc_dsl import (
    apply,
    canvas,
    fgpartition,
    lbind,
    mapply,
    merge,
    mostcolor,
    multiply,
    normalize,
    paint,
    rbind,
    shape,
    shift,
    toindices,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "8f2ea7aa"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = fgpartition(grid)
    x1 = merge(x0)
    x2 = normalize(x1)
    x3 = mostcolor(grid)
    x4 = shape(x2)
    x5 = multiply(x4, x4)
    x6 = canvas(x3, x5)
    x7 = shape(x2)
    x8 = rbind(multiply, x7)
    x9 = toindices(x2)
    x10 = apply(x8, x9)
    x11 = lbind(shift, x2)
    x12 = mapply(x11, x10)
    x13 = paint(x6, x12)
    return x13


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
