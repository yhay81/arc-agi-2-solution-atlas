"""Executable re-arc DSL program for ARC-AGI-2 task ac0a08a4.

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
    colorcount,
    height,
    mostcolor,
    multiply,
    subtract,
    upscale,
    width,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "ac0a08a4"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = mostcolor(grid)
    x1 = colorcount(grid, x0)
    x2 = height(grid)
    x3 = width(grid)
    x4 = multiply(x2, x3)
    x5 = subtract(x4, x1)
    x6 = upscale(grid, x5)
    return x6


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
