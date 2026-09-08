"""Executable re-arc DSL program for ARC-AGI-2 task 1a07d186.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.re_arc_dsl import (
    apply,
    asindices,
    color,
    colorfilter,
    compose,
    difference,
    fill,
    fork,
    frontiers,
    gravitate,
    identity,
    initset,
    lbind,
    mapply,
    mostcolor,
    ofcolor,
    paint,
    rbind,
    shift,
    toindices,
    toobject,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "1a07d186"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = frontiers(grid)
    x1 = mostcolor(grid)
    x2 = asindices(grid)
    x3 = ofcolor(grid, x1)
    x4 = difference(x2, x3)
    x5 = mapply(toindices, x0)
    x6 = difference(x4, x5)
    x7 = toobject(x6, grid)
    x8 = apply(initset, x7)
    x9 = fill(grid, x1, x6)
    x10 = lbind(fork, shift)
    x11 = lbind(x10, identity)
    x12 = lbind(rbind, gravitate)
    x13 = compose(x11, x12)
    x14 = lbind(colorfilter, x8)
    x15 = compose(x14, color)
    x16 = fork(mapply, x13, x15)
    x17 = mapply(x16, x0)
    x18 = paint(x9, x17)
    return x18


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
