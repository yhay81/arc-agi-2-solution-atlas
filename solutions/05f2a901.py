"""Executable re-arc DSL program for ARC-AGI-2 task 05f2a901.

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
    T,
    equality,
    extract,
    fork,
    gravitate,
    height,
    move,
    multiply,
    objects,
    other,
    size,
    width,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "05f2a901"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, T, T)
    x1 = fork(multiply, height, width)
    x2 = fork(equality, size, x1)
    x3 = extract(x0, x2)
    x4 = other(x0, x3)
    x5 = gravitate(x4, x3)
    x6 = move(grid, x4, x5)
    return x6


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
