"""Executable re-arc DSL program for ARC-AGI-2 task 8e1813be.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    apply,
    branch,
    color,
    dmirror,
    either,
    fork,
    greater,
    height,
    identity,
    leftmost,
    matcher,
    order,
    partition,
    repeat,
    sfilter,
    size,
    uppermost,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "8e1813be"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = partition(grid)
    x1 = matcher(height, ONE)
    x2 = matcher(width, ONE)
    x3 = fork(either, x1, x2)
    x4 = sfilter(x0, x3)
    x5 = matcher(height, ONE)
    x6 = sfilter(x4, x5)
    x7 = size(x6)
    x8 = matcher(width, ONE)
    x9 = sfilter(x4, x8)
    x10 = size(x9)
    x11 = greater(x7, x10)
    x12 = branch(x11, dmirror, identity)
    x13 = branch(x11, uppermost, leftmost)
    x14 = order(x4, x13)
    x15 = apply(color, x14)
    x16 = size(x4)
    x17 = repeat(x15, x16)
    x18 = x12(x17)
    return x18


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
