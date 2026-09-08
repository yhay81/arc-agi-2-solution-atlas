"""Executable re-arc DSL program for ARC-AGI-2 task a5313dff.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    F,
    T,
    apply,
    bordering,
    color,
    colorfilter,
    compose,
    fill,
    flip,
    mfilter,
    mostcolor,
    mostcommon,
    objects,
    rbind,
    sfilter,
    totuple,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "a5313dff"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, F)
    x1 = rbind(bordering, grid)
    x2 = compose(flip, x1)
    x3 = sfilter(x0, x2)
    x4 = totuple(x3)
    x5 = apply(color, x4)
    mostcommon(x5)
    x7 = mostcolor(grid)
    x8 = colorfilter(x0, x7)
    x9 = rbind(bordering, grid)
    x10 = compose(flip, x9)
    x11 = mfilter(x8, x10)
    x12 = fill(grid, ONE, x11)
    return x12


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
