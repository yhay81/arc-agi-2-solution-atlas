"""Executable re-arc DSL program for ARC-AGI-2 task b7249182.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    DOWN,
    NEG_TWO,
    UP,
    ZERO,
    ZERO_BY_TWO,
    F,
    T,
    add,
    astuple,
    branch,
    centerofmass,
    color,
    combine,
    compose,
    connect,
    cover,
    dmirror,
    fill,
    first,
    identity,
    initset,
    insert,
    last,
    llcorner,
    lrcorner,
    merge,
    objects,
    order,
    paint,
    portrait,
    shift,
    toindices,
    toobject,
    ulcorner,
    uppermost,
    urcorner,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "b7249182"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, T)
    x1 = merge(x0)
    x2 = portrait(x1)
    x3 = branch(x2, identity, dmirror)
    x4 = x3(grid)
    x5 = objects(x4, T, F, T)
    x6 = order(x5, uppermost)
    x7 = first(x6)
    x8 = last(x6)
    x9 = color(x7)
    x10 = color(x8)
    x11 = compose(first, toindices)
    x12 = x11(x7)
    x13 = x11(x8)
    x14 = connect(x12, x13)
    x15 = centerofmass(x14)
    x16 = connect(x12, x15)
    x17 = fill(x4, x10, x14)
    x18 = fill(x17, x9, x16)
    x19 = add(x15, DOWN)
    x20 = initset(x15)
    x21 = insert(x19, x20)
    x22 = toobject(x21, x18)
    x23 = astuple(ZERO, NEG_TWO)
    x24 = shift(x22, ZERO_BY_TWO)
    x25 = shift(x22, x23)
    x26 = combine(x24, x25)
    x27 = ulcorner(x26)
    x28 = urcorner(x26)
    x29 = connect(x27, x28)
    x30 = shift(x29, UP)
    x31 = llcorner(x26)
    x32 = lrcorner(x26)
    x33 = connect(x31, x32)
    x34 = shift(x33, DOWN)
    x35 = paint(x18, x26)
    x36 = fill(x35, x9, x30)
    x37 = fill(x36, x10, x34)
    x38 = cover(x37, x21)
    x39 = x3(x38)
    return x39


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
