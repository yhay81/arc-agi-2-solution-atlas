"""Executable re-arc DSL program for ARC-AGI-2 task 22eb0ac0.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ZERO,
    apply,
    asindices,
    asobject,
    branch,
    center,
    color,
    compose,
    connect,
    decrement,
    either,
    equality,
    first,
    flip,
    fork,
    height,
    initset,
    last,
    leftmost,
    mapply,
    matcher,
    mostcolor,
    paint,
    product,
    recolor,
    sfilter,
    toindices,
    toobject,
    uppermost,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "22eb0ac0"
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
    x6 = product(x5, x5)
    x7 = compose(color, first)
    x8 = compose(color, last)
    x9 = fork(equality, x7, x8)
    x10 = sfilter(x6, x9)
    x11 = compose(leftmost, first)
    x12 = compose(leftmost, last)
    x13 = fork(equality, x11, x12)
    x14 = compose(uppermost, first)
    x15 = compose(uppermost, last)
    x16 = fork(equality, x14, x15)
    x17 = fork(either, x13, x16)
    x18 = sfilter(x10, x17)
    x19 = compose(color, first)
    x20 = compose(center, first)
    x21 = compose(center, last)
    x22 = fork(connect, x20, x21)
    x23 = fork(recolor, x19, x22)
    x24 = height(grid)
    x25 = width(grid)
    x26 = matcher(last, ZERO)
    x27 = decrement(x25)
    x28 = matcher(last, x27)
    x29 = fork(either, x26, x28)
    x30 = matcher(first, ZERO)
    x31 = decrement(x24)
    x32 = matcher(first, x31)
    x33 = fork(either, x30, x32)
    x34 = toindices(x4)
    x35 = sfilter(x34, x29)
    x36 = equality(x34, x35)
    x37 = mapply(x23, x18)
    x38 = paint(grid, x37)
    x39 = branch(x36, x29, x33)
    x40 = asindices(grid)
    x41 = sfilter(x40, x39)
    x42 = toobject(x41, grid)
    x43 = paint(x38, x42)
    return x43


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
