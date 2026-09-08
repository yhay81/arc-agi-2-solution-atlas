"""Executable re-arc DSL program for ARC-AGI-2 task 41e4d17e.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    NINE,
    SIX,
    F,
    T,
    both,
    center,
    combine,
    compose,
    equality,
    fork,
    height,
    hfrontier,
    lbind,
    mapply,
    objects,
    sfilter,
    size,
    underfill,
    vfrontier,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "41e4d17e"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = lbind(equality, NINE)
    x1 = compose(x0, size)
    x2 = fork(equality, height, width)
    x3 = fork(both, x1, x2)
    x4 = objects(grid, T, F, F)
    x5 = sfilter(x4, x3)
    x6 = fork(combine, vfrontier, hfrontier)
    x7 = compose(x6, center)
    x8 = mapply(x7, x5)
    x9 = underfill(grid, SIX, x8)
    return x9


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
