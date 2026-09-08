"""Executable re-arc DSL program for ARC-AGI-2 task b548a754.

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
    argmin,
    backdrop,
    both,
    box,
    color,
    combine,
    compose,
    equality,
    extract,
    fill,
    flip,
    fork,
    height,
    inbox,
    multiply,
    partition,
    remove,
    size,
    toindices,
    toobject,
    width,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "b548a754"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = partition(grid)
    x1 = fork(equality, toindices, box)
    x2 = fork(multiply, height, width)
    x3 = fork(equality, size, x2)
    x4 = compose(flip, x3)
    x5 = fork(both, x1, x4)
    x6 = extract(x0, x5)
    x7 = inbox(x6)
    x8 = backdrop(x7)
    x9 = toobject(x8, grid)
    x10 = remove(x9, x0)
    x11 = remove(x6, x10)
    x12 = argmin(x11, size)
    x13 = combine(x12, x6)
    x14 = backdrop(x13)
    x15 = color(x9)
    x16 = fill(grid, x15, x14)
    x17 = color(x6)
    x18 = box(x14)
    x19 = fill(x16, x17, x18)
    return x19


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
