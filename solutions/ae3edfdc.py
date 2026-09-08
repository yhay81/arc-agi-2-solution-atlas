"""Executable re-arc DSL program for ARC-AGI-2 task ae3edfdc.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    SEVEN,
    THREE,
    TWO,
    add,
    apply,
    center,
    chain,
    combine,
    compose,
    cover,
    fill,
    initset,
    invert,
    lbind,
    ofcolor,
    position,
    rbind,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "ae3edfdc"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = ofcolor(grid, ONE)
    x1 = center(x0)
    x2 = ofcolor(grid, TWO)
    x3 = center(x2)
    x4 = ofcolor(grid, THREE)
    x5 = ofcolor(grid, SEVEN)
    x6 = lbind(add, x1)
    x7 = initset(x1)
    x8 = rbind(position, x7)
    x9 = compose(invert, x8)
    x10 = chain(x6, x9, initset)
    x11 = lbind(add, x3)
    x12 = initset(x3)
    x13 = rbind(position, x12)
    x14 = compose(invert, x13)
    x15 = chain(x11, x14, initset)
    x16 = apply(x10, x5)
    x17 = apply(x15, x4)
    x18 = combine(x4, x5)
    x19 = cover(grid, x18)
    x20 = fill(x19, SEVEN, x16)
    x21 = fill(x20, THREE, x17)
    return x21


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
