"""Executable re-arc DSL program for ARC-AGI-2 task e73095fd.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    FOUR,
    ZERO,
    F,
    T,
    backdrop,
    chain,
    colorfilter,
    corners,
    difference,
    dneighbors,
    equality,
    fill,
    fork,
    intersection,
    lbind,
    leastcolor,
    mapply,
    matcher,
    mfilter,
    mostcolor,
    objects,
    ofcolor,
    outbox,
    rbind,
    sfilter,
    size,
    toindices,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "e73095fd"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, F)
    x1 = mostcolor(grid)
    x2 = colorfilter(x0, x1)
    x3 = fork(equality, toindices, backdrop)
    x4 = sfilter(x2, x3)
    x5 = lbind(mapply, dneighbors)
    x6 = chain(x5, corners, outbox)
    x7 = fork(difference, x6, outbox)
    x8 = leastcolor(grid)
    x9 = ofcolor(grid, x8)
    x10 = rbind(intersection, x9)
    x11 = matcher(size, ZERO)
    x12 = chain(x11, x10, x7)
    x13 = mfilter(x4, x12)
    x14 = fill(grid, FOUR, x13)
    return x14


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
