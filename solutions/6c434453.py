"""Executable re-arc DSL program for ARC-AGI-2 task 6c434453.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    TWO,
    F,
    T,
    backdrop,
    box,
    center,
    chain,
    combine,
    compose,
    equality,
    fill,
    fork,
    greater,
    hfrontier,
    intersection,
    mapply,
    merge,
    minimum,
    mostcolor,
    objects,
    rbind,
    sfilter,
    shape,
    toindices,
    vfrontier,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "6c434453"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, T)
    x1 = rbind(greater, TWO)
    x2 = chain(x1, minimum, shape)
    x3 = sfilter(x0, x2)
    x4 = fork(equality, toindices, box)
    x5 = sfilter(x3, x4)
    x6 = mostcolor(grid)
    x7 = merge(x5)
    x8 = fill(grid, x6, x7)
    x9 = compose(hfrontier, center)
    x10 = compose(vfrontier, center)
    x11 = fork(combine, x9, x10)
    x12 = fork(intersection, x11, backdrop)
    x13 = mapply(x12, x5)
    x14 = fill(x8, TWO, x13)
    return x14


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
