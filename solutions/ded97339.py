"""Executable re-arc DSL program for ARC-AGI-2 task ded97339.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    NEG_ONE,
    backdrop,
    chain,
    combine,
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

TASK_ID = "ded97339"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = leastcolor(grid)
    x1 = lbind(recolor, NEG_ONE)
    x2 = rbind(ofcolor, x0)
    x3 = chain(x1, backdrop, x2)
    x4 = fork(paint, identity, x3)
    x5 = height(grid)
    x6 = vsplit(grid, x5)
    x7 = mapply(x4, x6)
    x8 = ofcolor(x7, NEG_ONE)
    x9 = dmirror(grid)
    x10 = width(grid)
    x11 = vsplit(x9, x10)
    x12 = mapply(x4, x11)
    x13 = dmirror(x12)
    x14 = ofcolor(x13, NEG_ONE)
    x15 = combine(x8, x14)
    x16 = fill(grid, x0, x15)
    return x16


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
