"""Executable re-arc DSL program for ARC-AGI-2 task ce9e57f2.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    EIGHT,
    F,
    T,
    adjacent,
    asindices,
    chain,
    compose,
    extract,
    fill,
    fork,
    greater,
    halve,
    initset,
    lbind,
    manhattan,
    mapply,
    objects,
    outbox,
    rbind,
    sfilter,
    size,
    toindices,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "ce9e57f2"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, T)
    x1 = asindices(grid)
    x2 = outbox(x1)
    x3 = lbind(adjacent, x2)
    x4 = compose(x3, initset)
    x5 = rbind(extract, x4)
    x6 = compose(x5, toindices)
    x7 = rbind(compose, initset)
    x8 = lbind(rbind, manhattan)
    x9 = chain(x7, x8, initset)
    x10 = lbind(lbind, greater)
    x11 = chain(x10, halve, size)
    x12 = compose(x9, x6)
    x13 = fork(compose, x11, x12)
    x14 = fork(sfilter, toindices, x13)
    x15 = mapply(x14, x0)
    x16 = fill(grid, EIGHT, x15)
    return x16


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
