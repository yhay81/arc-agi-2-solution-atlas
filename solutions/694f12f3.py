"""Executable re-arc DSL program for ARC-AGI-2 task 694f12f3.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    TWO,
    F,
    T,
    argmax,
    argmin,
    backdrop,
    compose,
    equality,
    fill,
    fork,
    height,
    inbox,
    multiply,
    objects,
    sfilter,
    size,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "694f12f3"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, F)
    x1 = fork(multiply, height, width)
    x2 = fork(equality, size, x1)
    x3 = sfilter(x0, x2)
    x4 = compose(backdrop, inbox)
    x5 = argmin(x3, size)
    x6 = argmax(x3, size)
    x7 = x4(x5)
    x8 = x4(x6)
    x9 = fill(grid, ONE, x7)
    x10 = fill(x9, TWO, x8)
    return x10


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
