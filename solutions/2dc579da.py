"""Executable re-arc DSL program for ARC-AGI-2 task 2dc579da.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    DOWN_LEFT,
    NEG_UNITY,
    ONE,
    ORIGIN,
    UNITY,
    UP_RIGHT,
    add,
    apply,
    astuple,
    backdrop,
    color,
    combine,
    compose,
    decrement,
    extract,
    flip,
    frontiers,
    height,
    hline,
    initset,
    insert,
    leftmost,
    lowermost,
    matcher,
    mfilter,
    mostcommon,
    numcolors,
    palette,
    rbind,
    rightmost,
    sfilter,
    shape,
    subgrid,
    toivec,
    tojvec,
    toobject,
    uppermost,
    vline,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "2dc579da"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = frontiers(grid)
    x1 = mfilter(x0, hline)
    x2 = mfilter(x0, vline)
    x3 = uppermost(x1)
    x4 = leftmost(x2)
    x5 = astuple(x3, x4)
    x6 = add(x5, NEG_UNITY)
    x7 = uppermost(x1)
    x8 = rightmost(x2)
    x9 = astuple(x7, x8)
    x10 = add(x9, UP_RIGHT)
    x11 = lowermost(x1)
    x12 = leftmost(x2)
    x13 = astuple(x11, x12)
    x14 = add(x13, DOWN_LEFT)
    x15 = lowermost(x1)
    x16 = rightmost(x2)
    x17 = astuple(x15, x16)
    x18 = add(x17, UNITY)
    x19 = initset(ORIGIN)
    x20 = insert(x6, x19)
    x21 = width(grid)
    x22 = decrement(x21)
    x23 = tojvec(x22)
    x24 = initset(x23)
    x25 = insert(x10, x24)
    x26 = height(grid)
    x27 = decrement(x26)
    x28 = toivec(x27)
    x29 = initset(x28)
    x30 = insert(x14, x29)
    x31 = shape(grid)
    x32 = decrement(x31)
    x33 = initset(x32)
    x34 = insert(x18, x33)
    x35 = astuple(x20, x25)
    x36 = astuple(x30, x34)
    x37 = combine(x35, x36)
    x38 = rbind(toobject, grid)
    x39 = compose(x38, backdrop)
    x40 = apply(x39, x37)
    x41 = matcher(numcolors, ONE)
    x42 = sfilter(x40, x41)
    x43 = apply(color, x42)
    x44 = mostcommon(x43)
    x45 = initset(x44)
    x46 = matcher(palette, x45)
    x47 = compose(flip, x46)
    x48 = extract(x40, x47)
    x49 = subgrid(x48, grid)
    return x49


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
