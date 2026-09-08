"""Executable re-arc DSL program for ARC-AGI-2 task d687bc17.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    NEG_ONE,
    UNITY,
    apply,
    asindices,
    asobject,
    chain,
    color,
    colorfilter,
    combine,
    compose,
    contained,
    corners,
    fgpartition,
    fill,
    first,
    fork,
    gravitate,
    identity,
    initset,
    lbind,
    mapply,
    mostcolor,
    paint,
    rbind,
    sfilter,
    shift,
    toindices,
    toobject,
    trim,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "d687bc17"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = trim(grid)
    x1 = asobject(x0)
    x2 = shift(x1, UNITY)
    x3 = apply(initset, x2)
    x4 = toindices(x2)
    x5 = asindices(grid)
    x6 = corners(x5)
    x7 = combine(x4, x6)
    x8 = fill(grid, NEG_ONE, x7)
    x9 = fgpartition(x8)
    x10 = asindices(grid)
    x11 = corners(x10)
    x12 = toobject(x11, grid)
    x13 = combine(x2, x12)
    x14 = mostcolor(x13)
    x15 = fill(x8, x14, x7)
    x16 = apply(color, x9)
    x17 = rbind(contained, x16)
    x18 = compose(x17, color)
    x19 = sfilter(x3, x18)
    x20 = lbind(colorfilter, x9)
    x21 = chain(first, x20, color)
    x22 = fork(gravitate, identity, x21)
    x23 = fork(shift, identity, x22)
    x24 = mapply(x23, x19)
    x25 = paint(x15, x24)
    return x25


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
