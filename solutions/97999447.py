"""Executable re-arc DSL program for ARC-AGI-2 task 97999447.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    FIVE,
    ONE,
    RIGHT,
    ZERO,
    apply,
    asobject,
    center,
    color,
    compose,
    double,
    fill,
    first,
    flip,
    fork,
    increment,
    initset,
    interval,
    mapply,
    matcher,
    merge,
    mostcolor,
    paint,
    prapply,
    rbind,
    recolor,
    sfilter,
    shift,
    shoot,
    toindices,
    tojvec,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "97999447"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = mostcolor(grid)
    x1 = asobject(grid)
    x2 = matcher(first, x0)
    x3 = compose(flip, x2)
    x4 = sfilter(x1, x3)
    x5 = apply(initset, x4)
    x6 = apply(toindices, x5)
    x7 = rbind(shoot, RIGHT)
    x8 = compose(x7, center)
    x9 = fork(recolor, color, x8)
    x10 = mapply(x9, x5)
    x11 = paint(grid, x10)
    x12 = width(grid)
    x13 = interval(ZERO, x12, ONE)
    x14 = apply(double, x13)
    x15 = apply(increment, x14)
    x16 = apply(tojvec, x15)
    x17 = prapply(shift, x6, x16)
    x18 = merge(x17)
    x19 = fill(x11, FIVE, x18)
    return x19


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
