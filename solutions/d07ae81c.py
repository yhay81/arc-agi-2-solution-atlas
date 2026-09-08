"""Executable re-arc DSL program for ARC-AGI-2 task d07ae81c.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    DOWN_LEFT,
    NEG_UNITY,
    UNITY,
    UP_RIGHT,
    ZERO,
    combine,
    compose,
    fill,
    first,
    fork,
    intersection,
    last,
    lbind,
    mapply,
    matcher,
    mostcolor,
    neighbors,
    ofcolor,
    palette,
    rbind,
    sfilter,
    shoot,
    size,
    toobject,
    totuple,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "d07ae81c"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = lbind(ofcolor, grid)
    x1 = lbind(mapply, neighbors)
    x2 = compose(x1, x0)
    x3 = fork(intersection, x0, x2)
    x4 = compose(size, x3)
    x5 = palette(grid)
    x6 = matcher(x4, ZERO)
    x7 = sfilter(x5, x6)
    x8 = totuple(x7)
    x9 = first(x8)
    x10 = last(x8)
    x11 = ofcolor(grid, x9)
    x12 = mapply(neighbors, x11)
    x13 = toobject(x12, grid)
    x14 = mostcolor(x13)
    x15 = ofcolor(grid, x10)
    x16 = mapply(neighbors, x15)
    x17 = toobject(x16, grid)
    x18 = mostcolor(x17)
    x19 = rbind(shoot, UNITY)
    x20 = rbind(shoot, NEG_UNITY)
    x21 = fork(combine, x19, x20)
    x22 = rbind(shoot, UP_RIGHT)
    x23 = rbind(shoot, DOWN_LEFT)
    x24 = fork(combine, x22, x23)
    x25 = fork(combine, x21, x24)
    x26 = ofcolor(grid, x10)
    x27 = ofcolor(grid, x9)
    x28 = combine(x26, x27)
    x29 = mapply(x25, x28)
    x30 = ofcolor(grid, x14)
    x31 = intersection(x30, x29)
    x32 = ofcolor(grid, x18)
    x33 = intersection(x32, x29)
    x34 = fill(grid, x9, x31)
    x35 = fill(x34, x10, x33)
    return x35


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
