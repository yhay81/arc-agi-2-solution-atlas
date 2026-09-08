"""Executable re-arc DSL program for ARC-AGI-2 task dbc1a6ce.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    EIGHT,
    backdrop,
    chain,
    combine,
    difference,
    dmirror,
    fill,
    fork,
    height,
    identity,
    lbind,
    leastcolor,
    mapply,
    ofcolor,
    paint,
    rbind,
    recolor,
    vsplit,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "dbc1a6ce"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = leastcolor(grid)
    x1 = ofcolor(grid, x0)
    x2 = lbind(recolor, EIGHT)
    x3 = rbind(ofcolor, x0)
    x4 = chain(x2, backdrop, x3)
    x5 = fork(paint, identity, x4)
    x6 = height(grid)
    x7 = vsplit(grid, x6)
    x8 = mapply(x5, x7)
    x9 = ofcolor(x8, EIGHT)
    x10 = dmirror(grid)
    x11 = width(grid)
    x12 = vsplit(x10, x11)
    x13 = mapply(x5, x12)
    x14 = dmirror(x13)
    x15 = ofcolor(x14, EIGHT)
    x16 = combine(x9, x15)
    x17 = difference(x16, x1)
    x18 = fill(grid, EIGHT, x17)
    return x18


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
