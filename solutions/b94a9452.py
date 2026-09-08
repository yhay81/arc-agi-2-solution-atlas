"""Executable re-arc DSL program for ARC-AGI-2 task b94a9452.

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
    argmax,
    fork,
    height,
    leastcolor,
    merge,
    mostcolor,
    multiply,
    partition,
    remove,
    subgrid,
    switch,
    width,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "b94a9452"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = partition(grid)
    x1 = fork(multiply, height, width)
    x2 = argmax(x0, x1)
    x3 = remove(x2, x0)
    x4 = merge(x3)
    x5 = subgrid(x4, grid)
    x6 = mostcolor(x5)
    x7 = leastcolor(x5)
    x8 = switch(x5, x6, x7)
    return x8


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
