"""Executable re-arc DSL program for ARC-AGI-2 task 5c0a986e.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    NEG_UNITY,
    ONE,
    TWO,
    UNITY,
    F,
    T,
    chain,
    colorfilter,
    combine,
    lbind,
    lrcorner,
    mapply,
    objects,
    paint,
    rbind,
    recolor,
    shoot,
    ulcorner,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "5c0a986e"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, T)
    x1 = colorfilter(x0, TWO)
    x2 = colorfilter(x0, ONE)
    x3 = lbind(recolor, TWO)
    x4 = rbind(shoot, UNITY)
    x5 = chain(x3, x4, lrcorner)
    x6 = lbind(recolor, ONE)
    x7 = rbind(shoot, NEG_UNITY)
    x8 = chain(x6, x7, ulcorner)
    x9 = mapply(x5, x1)
    x10 = mapply(x8, x2)
    x11 = combine(x9, x10)
    x12 = paint(grid, x11)
    return x12


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
