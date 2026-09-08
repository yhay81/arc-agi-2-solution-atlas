"""Executable re-arc DSL program for ARC-AGI-2 task 1caeab9d.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    T,
    chain,
    cover,
    fork,
    identity,
    lbind,
    lowermost,
    mapply,
    merge,
    objects,
    ofcolor,
    paint,
    shift,
    subtract,
    toivec,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "1caeab9d"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, T, T)
    x1 = ofcolor(grid, ONE)
    x2 = lowermost(x1)
    x3 = lbind(subtract, x2)
    x4 = chain(toivec, x3, lowermost)
    x5 = fork(shift, identity, x4)
    x6 = merge(x0)
    x7 = cover(grid, x6)
    x8 = mapply(x5, x0)
    x9 = paint(x7, x8)
    return x9


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
