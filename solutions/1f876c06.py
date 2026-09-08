"""Executable re-arc DSL program for ARC-AGI-2 task 1f876c06.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    TWO,
    color,
    compose,
    connect,
    fgpartition,
    first,
    fork,
    last,
    mapply,
    paint,
    power,
    recolor,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "1f876c06"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = fgpartition(grid)
    x1 = compose(last, first)
    x2 = power(last, TWO)
    x3 = fork(connect, x1, x2)
    x4 = fork(recolor, color, x3)
    x5 = mapply(x4, x0)
    x6 = paint(grid, x5)
    return x6


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
