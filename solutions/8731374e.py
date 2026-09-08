"""Executable re-arc DSL program for ARC-AGI-2 task 8731374e.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    DOWN,
    EIGHT,
    TWO,
    F,
    T,
    argmax,
    asindices,
    branch,
    chain,
    color,
    combine,
    compose,
    double,
    fill,
    first,
    fork,
    greater,
    hfrontier,
    identity,
    initset,
    insert,
    lbind,
    leastcolor,
    lrcorner,
    mapply,
    matcher,
    objects,
    ofcolor,
    power,
    rapply,
    rbind,
    rot90,
    sfilter,
    size,
    subgrid,
    subtract,
    vfrontier,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "8731374e"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, F)
    x1 = argmax(x0, size)
    x2 = color(x1)
    x3 = subgrid(x1, grid)
    x4 = lbind(insert, DOWN)
    x5 = compose(lrcorner, asindices)
    x6 = chain(x4, initset, x5)
    x7 = fork(subgrid, x6, identity)
    x8 = matcher(identity, x2)
    x9 = rbind(subtract, TWO)
    x10 = rbind(sfilter, x8)
    x11 = compose(x9, width)
    x12 = chain(size, x10, first)
    x13 = fork(greater, x11, x12)
    x14 = rbind(branch, identity)
    x15 = rbind(x14, x7)
    x16 = chain(initset, x15, x13)
    x17 = fork(rapply, x16, identity)
    x18 = compose(first, x17)
    x19 = compose(x18, rot90)
    x20 = double(EIGHT)
    x21 = double(x20)
    x22 = power(x19, x21)
    x23 = x22(x3)
    x24 = leastcolor(x23)
    x25 = ofcolor(x23, x24)
    x26 = fork(combine, vfrontier, hfrontier)
    x27 = mapply(x26, x25)
    x28 = fill(x23, x24, x27)
    return x28


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
