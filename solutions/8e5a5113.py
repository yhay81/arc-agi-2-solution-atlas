"""Executable re-arc DSL program for ARC-AGI-2 task 8e5a5113.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    FOUR,
    ONE,
    F,
    T,
    add,
    argmax,
    asobject,
    branch,
    canvas,
    chain,
    combine,
    compose,
    first,
    fork,
    hconcat,
    height,
    identity,
    increment,
    index,
    initset,
    interval,
    lbind,
    mapply,
    multiply,
    numcolors,
    objects,
    paint,
    portrait,
    power,
    rapply,
    rbind,
    rot90,
    rot270,
    shape,
    shift,
    subgrid,
    subtract,
    toivec,
    uppermost,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "8e5a5113"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = portrait(grid)
    x1 = branch(x0, identity, rot90)
    x2 = branch(x0, identity, rot270)
    x3 = x1(grid)
    x4 = width(x3)
    x5 = toivec(x4)
    x6 = index(x3, x5)
    x7 = shape(x3)
    x8 = canvas(x6, x7)
    x9 = hconcat(x3, x8)
    x10 = objects(x9, F, T, T)
    x11 = argmax(x10, numcolors)
    x12 = subgrid(x11, x3)
    x13 = interval(ONE, FOUR, ONE)
    x14 = lbind(power, rot90)
    x15 = lbind(power, rot270)
    x16 = rbind(rapply, x12)
    x17 = compose(initset, x14)
    x18 = chain(first, x16, x17)
    x19 = rbind(rapply, x12)
    x20 = compose(initset, x15)
    x21 = chain(first, x19, x20)
    x22 = compose(asobject, x18)
    x23 = uppermost(x11)
    x24 = lbind(add, x23)
    x25 = height(x11)
    x26 = increment(x25)
    x27 = lbind(multiply, x26)
    x28 = chain(toivec, x24, x27)
    x29 = fork(shift, x22, x28)
    x30 = compose(asobject, x21)
    x31 = uppermost(x11)
    x32 = lbind(subtract, x31)
    x33 = height(x11)
    x34 = increment(x33)
    x35 = lbind(multiply, x34)
    x36 = chain(toivec, x32, x35)
    x37 = fork(shift, x30, x36)
    x38 = fork(combine, x29, x37)
    x39 = mapply(x38, x13)
    x40 = paint(x3, x39)
    x41 = x2(x40)
    return x41


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
