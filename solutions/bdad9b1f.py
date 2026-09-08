"""Executable re-arc DSL program for ARC-AGI-2 task bdad9b1f.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    FOUR,
    F,
    T,
    center,
    color,
    combine,
    compose,
    fill,
    fork,
    hfrontier,
    hline,
    intersection,
    mapply,
    objects,
    paint,
    recolor,
    sfilter,
    toindices,
    vfrontier,
    vline,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "bdad9b1f"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, T)
    x1 = sfilter(x0, hline)
    x2 = sfilter(x0, vline)
    x3 = compose(hfrontier, center)
    x4 = fork(recolor, color, x3)
    x5 = mapply(x4, x1)
    x6 = compose(vfrontier, center)
    x7 = fork(recolor, color, x6)
    x8 = mapply(x7, x2)
    x9 = combine(x5, x8)
    x10 = paint(grid, x9)
    x11 = toindices(x5)
    x12 = toindices(x8)
    x13 = intersection(x11, x12)
    x14 = fill(x10, FOUR, x13)
    return x14


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
