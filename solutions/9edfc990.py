"""Executable re-arc DSL program for ARC-AGI-2 task 9edfc990.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    ZERO,
    F,
    T,
    adjacent,
    colorfilter,
    mfilter,
    objects,
    ofcolor,
    paint,
    rbind,
    recolor,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "9edfc990"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, F)
    x1 = colorfilter(x0, ZERO)
    x2 = ofcolor(grid, ONE)
    x3 = rbind(adjacent, x2)
    x4 = mfilter(x1, x3)
    x5 = recolor(ONE, x4)
    x6 = paint(grid, x5)
    return x6


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
