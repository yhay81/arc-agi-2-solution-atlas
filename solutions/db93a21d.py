"""Executable re-arc DSL program for ARC-AGI-2 task db93a21d.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    DOWN,
    ONE,
    THREE,
    T,
    backdrop,
    chain,
    compose,
    difference,
    fill,
    first,
    fork,
    halve,
    identity,
    initset,
    intersection,
    lbind,
    mapply,
    merge,
    mostcolor,
    objects,
    ofcolor,
    outbox,
    power,
    rapply,
    rbind,
    shoot,
    toindices,
    underfill,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "db93a21d"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, T, T)
    x1 = merge(x0)
    x2 = toindices(x1)
    x3 = rbind(shoot, DOWN)
    x4 = mapply(x3, x2)
    x5 = underfill(grid, ONE, x4)
    x6 = lbind(power, outbox)
    x7 = chain(x6, halve, width)
    x8 = initset(x7)
    x9 = lbind(rapply, x8)
    x10 = fork(rapply, x9, identity)
    x11 = compose(first, x10)
    x12 = compose(backdrop, x11)
    x13 = fork(difference, x12, toindices)
    x14 = mapply(x13, x0)
    x15 = mostcolor(grid)
    x16 = ofcolor(grid, x15)
    x17 = intersection(x14, x16)
    x18 = fill(x5, THREE, x17)
    return x18


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
