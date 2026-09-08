"""Executable re-arc DSL program for ARC-AGI-2 task c909285e.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    argmin,
    box,
    chain,
    contained,
    equality,
    flip,
    fork,
    height,
    lbind,
    multiply,
    partition,
    sfilter,
    shape,
    subgrid,
    toindices,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "c909285e"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = partition(grid)
    x1 = lbind(contained, ONE)
    x2 = chain(flip, x1, shape)
    x3 = sfilter(x0, x2)
    x4 = fork(equality, toindices, box)
    x5 = sfilter(x3, x4)
    x6 = fork(multiply, height, width)
    x7 = argmin(x5, x6)
    x8 = subgrid(x7, grid)
    return x8


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
