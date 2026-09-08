"""Executable re-arc DSL program for ARC-AGI-2 task d4f3cd78.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    EIGHT,
    add,
    astuple,
    backdrop,
    box,
    combine,
    compose,
    difference,
    fgpartition,
    fill,
    first,
    fork,
    greater,
    identity,
    inbox,
    initset,
    invert,
    last,
    lbind,
    leftmost,
    lowermost,
    mapply,
    merge,
    position,
    rbind,
    rightmost,
    shoot,
    toindices,
    uppermost,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "d4f3cd78"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = fgpartition(grid)
    x1 = merge(x0)
    x2 = toindices(x1)
    x3 = box(x2)
    x4 = difference(x3, x2)
    x5 = inbox(x2)
    x6 = backdrop(x5)
    x7 = lbind(position, x6)
    compose(x7, initset)
    x9 = lowermost(x6)
    x10 = rightmost(x6)
    x11 = uppermost(x6)
    x12 = leftmost(x6)
    x13 = rbind(greater, x9)
    x14 = compose(x13, first)
    x15 = lbind(greater, x11)
    x16 = compose(x15, first)
    x17 = rbind(greater, x10)
    x18 = compose(x17, last)
    x19 = lbind(greater, x12)
    x20 = compose(x19, last)
    x21 = compose(invert, x16)
    x22 = fork(add, x14, x21)
    x23 = compose(invert, x20)
    x24 = fork(add, x18, x23)
    x25 = fork(astuple, x22, x24)
    x26 = fork(shoot, identity, x25)
    x27 = mapply(x26, x4)
    x28 = combine(x27, x6)
    x29 = fill(grid, EIGHT, x28)
    return x29


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
