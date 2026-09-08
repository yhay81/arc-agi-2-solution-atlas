"""Executable re-arc DSL program for ARC-AGI-2 task 469497ad.

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
    TWO,
    UNITY,
    UP_RIGHT,
    argmin,
    chain,
    combine,
    compose,
    decrement,
    fill,
    fork,
    height,
    intersection,
    lbind,
    llcorner,
    lrcorner,
    matcher,
    mostcolor,
    multiply,
    numcolors,
    ofcolor,
    outbox,
    palette,
    rbind,
    sfilter,
    shoot,
    toobject,
    ulcorner,
    upscale,
    urcorner,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "469497ad"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = numcolors(grid)
    x1 = decrement(x0)
    x2 = upscale(grid, x1)
    x3 = rbind(toobject, grid)
    x4 = lbind(ofcolor, grid)
    x5 = compose(outbox, x4)
    x6 = chain(numcolors, x3, x5)
    x7 = matcher(x6, ONE)
    x8 = palette(grid)
    x9 = sfilter(x8, x7)
    x10 = fork(multiply, height, width)
    x11 = lbind(ofcolor, grid)
    x12 = compose(x10, x11)
    x13 = argmin(x9, x12)
    x14 = ofcolor(x2, x13)
    x15 = outbox(x14)
    x16 = toobject(x15, x2)
    x17 = mostcolor(x16)
    x18 = ulcorner(x14)
    x19 = shoot(x18, NEG_UNITY)
    x20 = lrcorner(x14)
    x21 = shoot(x20, UNITY)
    x22 = urcorner(x14)
    x23 = shoot(x22, UP_RIGHT)
    x24 = llcorner(x14)
    x25 = shoot(x24, DOWN_LEFT)
    x26 = combine(x19, x21)
    x27 = combine(x23, x25)
    x28 = combine(x26, x27)
    x29 = ofcolor(x2, x17)
    x30 = intersection(x28, x29)
    x31 = fill(x2, TWO, x30)
    return x31


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
