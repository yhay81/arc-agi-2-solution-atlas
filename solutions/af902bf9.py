"""Executable re-arc DSL program for ARC-AGI-2 task af902bf9.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    NEG_ONE,
    ONE,
    SEVEN,
    THREE,
    TWO,
    asindices,
    astuple,
    backdrop,
    canvas,
    chain,
    combine,
    compose,
    corners,
    difference,
    first,
    fork,
    inbox,
    interval,
    last,
    lbind,
    mapply,
    mostcolor,
    multiply,
    occurrences,
    order,
    paint,
    palette,
    power,
    product,
    rbind,
    recolor,
    remove,
    shift,
    size,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "af902bf9"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = mostcolor(grid)
    x1 = palette(grid)
    x2 = remove(x0, x1)
    x3 = interval(THREE, SEVEN, ONE)
    x4 = product(x3, x3)
    x5 = fork(multiply, first, last)
    x6 = order(x4, x5)
    x7 = lbind(canvas, NEG_ONE)
    x8 = chain(x7, first, first)
    x9 = chain(corners, asindices, x8)
    x10 = lbind(recolor, x0)
    x11 = compose(asindices, x8)
    x12 = fork(difference, x11, x9)
    x13 = lbind(recolor, TWO)
    x14 = compose(inbox, x9)
    x15 = chain(x13, backdrop, x14)
    x16 = compose(x10, x12)
    x17 = lbind(lbind, combine)
    x18 = compose(x17, x16)
    x19 = lbind(rbind, recolor)
    x20 = compose(x19, x9)
    x21 = fork(compose, x18, x20)
    x22 = lbind(lbind, mapply)
    x23 = lbind(lbind, shift)
    x24 = chain(x22, x23, x15)
    x25 = lbind(lbind, occurrences)
    x26 = compose(x25, last)
    x27 = fork(compose, x26, x21)
    x28 = fork(compose, x24, x27)
    x29 = rbind(mapply, x2)
    x30 = compose(x29, x28)
    x31 = fork(paint, last, x30)
    x32 = compose(first, first)
    x33 = fork(remove, x32, first)
    x34 = fork(astuple, x33, x31)
    x35 = size(x6)
    x36 = power(x34, x35)
    x37 = astuple(x6, grid)
    x38 = x36(x37)
    x39 = last(x38)
    return x39


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
