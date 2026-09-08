"""Executable re-arc DSL program for ARC-AGI-2 task 776ffc46.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    F,
    T,
    argmax,
    backdrop,
    box,
    color,
    compose,
    equality,
    fill,
    first,
    flip,
    fork,
    height,
    inbox,
    matcher,
    mfilter,
    mostcolor,
    multiply,
    normalize,
    objects,
    sfilter,
    toindices,
    toobject,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "776ffc46"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, T)
    x1 = fork(equality, toindices, box)
    x2 = sfilter(x0, x1)
    x3 = fork(multiply, height, width)
    x4 = argmax(x2, x3)
    x5 = mostcolor(grid)
    x6 = inbox(x4)
    x7 = backdrop(x6)
    x8 = toobject(x7, grid)
    x9 = matcher(first, x5)
    x10 = compose(flip, x9)
    x11 = sfilter(x8, x10)
    x12 = normalize(x11)
    x13 = color(x12)
    x14 = toindices(x12)
    x15 = compose(toindices, normalize)
    x16 = matcher(x15, x14)
    x17 = mfilter(x0, x16)
    x18 = fill(grid, x13, x17)
    return x18


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
