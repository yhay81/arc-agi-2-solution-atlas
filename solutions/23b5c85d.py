"""Executable re-arc DSL program for ARC-AGI-2 task 23b5c85d.

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
    argmin,
    equality,
    fork,
    height,
    multiply,
    partition,
    sfilter,
    size,
    subgrid,
    width,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "23b5c85d"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = partition(grid)
    x1 = fork(multiply, height, width)
    x2 = fork(equality, size, x1)
    x3 = sfilter(x0, x2)
    x4 = argmin(x3, x1)
    x5 = subgrid(x4, grid)
    return x5


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
