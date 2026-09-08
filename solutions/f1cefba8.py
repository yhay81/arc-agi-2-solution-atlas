"""Executable re-arc DSL program for ARC-AGI-2 task f1cefba8.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.re_arc_dsl import (
    argmax,
    argmin,
    color,
    combine,
    corners,
    difference,
    fill,
    fork,
    height,
    hfrontier,
    inbox,
    intersection,
    mapply,
    multiply,
    other,
    partition,
    remove,
    toindices,
    vfrontier,
    width,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "f1cefba8"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = partition(grid)
    x1 = fork(multiply, height, width)
    x2 = argmax(x0, x1)
    x3 = argmin(x0, x1)
    x4 = remove(x2, x0)
    x5 = other(x4, x3)
    x6 = color(x3)
    x7 = color(x5)
    x8 = toindices(x3)
    x9 = inbox(x5)
    x10 = intersection(x8, x9)
    x11 = fork(combine, hfrontier, vfrontier)
    x12 = mapply(x11, x10)
    x13 = corners(x5)
    x14 = inbox(x5)
    x15 = corners(x14)
    x16 = combine(x13, x15)
    x17 = mapply(x11, x16)
    x18 = difference(x12, x17)
    x19 = toindices(x2)
    x20 = intersection(x18, x19)
    x21 = fill(grid, x6, x20)
    x22 = difference(x18, x20)
    x23 = fill(x21, x7, x22)
    x24 = inbox(x5)
    x25 = fill(x23, x7, x24)
    return x25


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
