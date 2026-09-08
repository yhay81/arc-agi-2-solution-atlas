"""Executable re-arc DSL program for ARC-AGI-2 task b6afb2da.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    FOUR,
    ONE,
    TWO,
    F,
    T,
    backdrop,
    box,
    color,
    compose,
    corners,
    equality,
    extract,
    fill,
    flip,
    fork,
    mapply,
    matcher,
    merge,
    objects,
    sfilter,
    toindices,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "b6afb2da"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, F)
    x1 = fork(equality, toindices, backdrop)
    x2 = compose(flip, x1)
    x3 = extract(x0, x2)
    x4 = color(x3)
    x5 = matcher(color, x4)
    x6 = compose(flip, x5)
    x7 = sfilter(x0, x6)
    x8 = merge(x7)
    x9 = fill(grid, TWO, x8)
    x10 = mapply(box, x7)
    x11 = fill(x9, FOUR, x10)
    x12 = mapply(corners, x7)
    x13 = fill(x11, ONE, x12)
    return x13


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
