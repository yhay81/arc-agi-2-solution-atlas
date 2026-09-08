"""Executable re-arc DSL program for ARC-AGI-2 task b527c5c6.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    F,
    T,
    backdrop,
    center,
    chain,
    combine,
    compose,
    decrement,
    difference,
    dneighbors,
    first,
    fork,
    identity,
    initset,
    intersection,
    invert,
    lbind,
    leastcolor,
    mapply,
    matcher,
    mostcolor,
    objects,
    outbox,
    paint,
    power,
    rapply,
    recolor,
    sfilter,
    shoot,
    size,
    subtract,
    toindices,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "b527c5c6"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, F, F, T)
    x1 = lbind(matcher, first)
    x2 = compose(x1, leastcolor)
    x3 = fork(sfilter, identity, x2)
    x4 = compose(center, x3)
    x5 = compose(dneighbors, x4)
    x6 = fork(difference, x5, toindices)
    x7 = compose(first, x6)
    x8 = fork(subtract, x7, x4)
    x9 = compose(invert, x8)
    x10 = fork(shoot, x4, x9)
    x11 = fork(intersection, toindices, x10)
    x12 = chain(decrement, size, x11)
    x13 = fork(shoot, x4, x8)
    x14 = lbind(power, outbox)
    x15 = compose(x14, x12)
    x16 = compose(initset, x15)
    x17 = fork(rapply, x16, x13)
    x18 = chain(backdrop, first, x17)
    x19 = fork(recolor, leastcolor, x13)
    x20 = fork(difference, x18, x13)
    x21 = fork(recolor, mostcolor, x20)
    x22 = fork(combine, x19, x21)
    x23 = mapply(x22, x0)
    x24 = paint(grid, x23)
    return x24


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
