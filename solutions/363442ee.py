"""Executable re-arc DSL program for ARC-AGI-2 task 363442ee.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    F,
    T,
    apply,
    argmax,
    center,
    fill,
    frontiers,
    halve,
    invert,
    lbind,
    mapply,
    merge,
    mostcolor,
    normalize,
    objects,
    paint,
    remove,
    shape,
    shift,
    size,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "363442ee"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = frontiers(grid)
    x1 = merge(x0)
    x2 = mostcolor(grid)
    x3 = fill(grid, x2, x1)
    x4 = objects(x3, F, F, T)
    x5 = argmax(x4, size)
    x6 = remove(x5, x4)
    x7 = apply(center, x6)
    x8 = normalize(x5)
    x9 = shape(x5)
    x10 = halve(x9)
    x11 = invert(x10)
    x12 = shift(x8, x11)
    x13 = lbind(shift, x12)
    x14 = mapply(x13, x7)
    x15 = paint(grid, x14)
    return x15


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
