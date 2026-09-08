"""Executable re-arc DSL program for ARC-AGI-2 task 7b6016b9.

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
    asindices,
    bordering,
    box,
    colorfilter,
    compose,
    fill,
    flip,
    mfilter,
    mostcolor,
    objects,
    rbind,
    replace,
    toobject,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "7b6016b9"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, F)
    x1 = asindices(grid)
    x2 = box(x1)
    x3 = toobject(x2, grid)
    x4 = mostcolor(x3)
    x5 = colorfilter(x0, x4)
    x6 = rbind(bordering, grid)
    x7 = compose(flip, x6)
    x8 = mfilter(x5, x7)
    x9 = fill(grid, TWO, x8)
    x10 = replace(x9, x4, THREE)
    return x10


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
