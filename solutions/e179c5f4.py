"""Executable re-arc DSL program for ARC-AGI-2 task e179c5f4.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    DOWN_LEFT,
    EIGHT,
    ONE,
    ORIGIN,
    UNITY,
    ZERO,
    asindices,
    astuple,
    branch,
    chain,
    combine,
    contained,
    corners,
    difference,
    divide,
    dmirror,
    equality,
    fill,
    first,
    height,
    hmirror,
    identity,
    increment,
    index,
    intersection,
    interval,
    last,
    lbind,
    llcorner,
    lrcorner,
    mapply,
    mostcolor,
    multiply,
    other,
    pair,
    palette,
    portrait,
    rbind,
    remove,
    replace,
    sfilter,
    shift,
    shoot,
    toivec,
    toobject,
    ulcorner,
    urcorner,
    vmirror,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "e179c5f4"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = portrait(grid)
    x1 = branch(x0, identity, dmirror)
    x2 = x1(grid)
    x3 = asindices(x2)
    x4 = shoot(ORIGIN, UNITY)
    x5 = intersection(x4, x3)
    x6 = lrcorner(x5)
    x7 = shoot(x6, DOWN_LEFT)
    x8 = intersection(x7, x3)
    x9 = combine(x5, x8)
    x10 = llcorner(x9)
    x11 = remove(x10, x9)
    x12 = lbind(shift, x11)
    x13 = height(x11)
    x14 = lbind(multiply, x13)
    x15 = chain(x12, toivec, x14)
    x16 = height(x2)
    x17 = height(x11)
    x18 = divide(x16, x17)
    x19 = increment(x18)
    x20 = interval(ZERO, x19, ONE)
    x21 = mapply(x15, x20)
    x22 = rbind(contained, x21)
    x23 = sfilter(x3, x22)
    x24 = asindices(grid)
    x25 = corners(x24)
    x26 = difference(x24, x25)
    x27 = toobject(x26, grid)
    x28 = mostcolor(x27)
    x29 = palette(grid)
    x30 = other(x29, x28)
    x31 = ulcorner(x3)
    x32 = index(x2, x31)
    x33 = equality(x32, x30)
    x34 = urcorner(x3)
    x35 = index(x2, x34)
    x36 = equality(x35, x30)
    x37 = llcorner(x3)
    x38 = index(x2, x37)
    x39 = equality(x38, x30)
    x40 = lrcorner(x3)
    x41 = index(x2, x40)
    x42 = equality(x41, x30)
    x43 = astuple(x33, x36)
    x44 = astuple(x39, x42)
    x45 = combine(x43, x44)
    x46 = vmirror(x23)
    x47 = astuple(x23, x46)
    x48 = hmirror(x23)
    x49 = hmirror(x46)
    x50 = astuple(x48, x49)
    x51 = combine(x47, x50)
    x52 = pair(x45, x51)
    x53 = sfilter(x52, first)
    x54 = mapply(last, x53)
    x55 = fill(x2, x30, x54)
    x56 = x1(x55)
    x57 = replace(x56, x28, EIGHT)
    return x57


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
