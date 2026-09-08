"""Executable re-arc DSL program for ARC-AGI-2 task 913fb3ed.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    EIGHT,
    FOUR,
    ONE,
    SIX,
    THREE,
    TWO,
    astuple,
    chain,
    first,
    fork,
    initset,
    insert,
    last,
    lbind,
    mapply,
    neighbors,
    ofcolor,
    paint,
    recolor,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "913fb3ed"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = lbind(ofcolor, grid)
    x1 = lbind(mapply, neighbors)
    x2 = chain(x1, x0, last)
    x3 = fork(recolor, first, x2)
    x4 = astuple(SIX, THREE)
    x5 = astuple(FOUR, EIGHT)
    x6 = astuple(ONE, TWO)
    x7 = initset(x4)
    x8 = insert(x5, x7)
    x9 = insert(x6, x8)
    x10 = mapply(x3, x9)
    x11 = paint(grid, x10)
    return x11


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
