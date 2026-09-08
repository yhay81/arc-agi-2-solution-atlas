"""Executable re-arc DSL program for ARC-AGI-2 task 22168020.

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
    compose,
    connect,
    fork,
    identity,
    lbind,
    mapply,
    merge,
    mostcolor,
    ofcolor,
    paint,
    palette,
    prapply,
    recolor,
    remove,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "22168020"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = palette(grid)
    x1 = mostcolor(grid)
    x2 = remove(x1, x0)
    x3 = lbind(ofcolor, grid)
    x4 = lbind(prapply, connect)
    x5 = fork(x4, x3, x3)
    x6 = compose(merge, x5)
    x7 = fork(recolor, identity, x6)
    x8 = mapply(x7, x2)
    x9 = paint(grid, x8)
    return x9


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
