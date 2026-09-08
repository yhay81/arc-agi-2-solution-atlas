"""Executable re-arc DSL program for ARC-AGI-2 task b2862040.

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
    apply,
    bordering,
    colorfilter,
    compose,
    difference,
    fill,
    flip,
    mfilter,
    mostcolor,
    objects,
    rbind,
    toindices,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "b2862040"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, F)
    x1 = mostcolor(grid)
    x2 = colorfilter(x0, x1)
    x3 = rbind(bordering, grid)
    x4 = compose(flip, x3)
    x5 = mfilter(x2, x4)
    x6 = difference(x0, x2)
    x7 = apply(toindices, x6)
    x8 = rbind(adjacent, x5)
    x9 = mfilter(x7, x8)
    x10 = fill(grid, EIGHT, x9)
    return x10


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
