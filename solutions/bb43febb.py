"""Executable re-arc DSL program for ARC-AGI-2 task bb43febb.

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
    backdrop,
    both,
    chain,
    compose,
    equality,
    fill,
    fork,
    greater,
    inbox,
    mapply,
    minimum,
    objects,
    rbind,
    sfilter,
    shape,
    toindices,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "bb43febb"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, F)
    x1 = fork(equality, toindices, backdrop)
    x2 = rbind(greater, ONE)
    x3 = chain(x2, minimum, shape)
    x4 = fork(both, x1, x3)
    x5 = sfilter(x0, x4)
    x6 = compose(backdrop, inbox)
    x7 = mapply(x6, x5)
    x8 = fill(grid, TWO, x7)
    return x8


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
