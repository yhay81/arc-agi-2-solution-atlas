"""Executable re-arc DSL program for ARC-AGI-2 task 91714a58.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ORIGIN,
    RIGHT,
    ZERO_BY_TWO,
    F,
    T,
    argmax,
    asindices,
    astuple,
    canvas,
    color,
    combine,
    dmirror,
    fill,
    initset,
    insert,
    lbind,
    mapply,
    mostcolor,
    objects,
    occurrences,
    paint,
    shape,
    shift,
    size,
    toindices,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "91714a58"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = shape(grid)
    asindices(grid)
    x2 = objects(grid, T, F, T)
    x3 = argmax(x2, size)
    mostcolor(x3)
    x5 = mostcolor(grid)
    x6 = canvas(x5, x0)
    x7 = paint(x6, x3)
    x8 = mostcolor(grid)
    x9 = color(x3)
    x10 = astuple(x8, ORIGIN)
    x11 = astuple(x9, RIGHT)
    x12 = astuple(x8, ZERO_BY_TWO)
    x13 = initset(x12)
    x14 = insert(x11, x13)
    x15 = insert(x10, x14)
    x16 = dmirror(x15)
    x17 = toindices(x15)
    x18 = lbind(shift, x17)
    x19 = occurrences(x7, x15)
    x20 = mapply(x18, x19)
    x21 = toindices(x16)
    x22 = lbind(shift, x21)
    x23 = occurrences(x7, x16)
    x24 = mapply(x22, x23)
    x25 = combine(x20, x24)
    x26 = fill(x7, x8, x25)
    return x26


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
