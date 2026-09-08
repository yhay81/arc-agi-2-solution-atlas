"""Executable re-arc DSL program for ARC-AGI-2 task 810b9b61.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    THREE,
    TWO,
    F,
    T,
    both,
    box,
    chain,
    equality,
    fill,
    fork,
    greater,
    mfilter,
    minimum,
    objects,
    rbind,
    shape,
    toindices,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "810b9b61"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, T)
    x1 = rbind(greater, TWO)
    x2 = chain(x1, minimum, shape)
    x3 = fork(equality, toindices, box)
    x4 = fork(both, x2, x3)
    x5 = mfilter(x0, x4)
    x6 = fill(grid, THREE, x5)
    return x6


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
