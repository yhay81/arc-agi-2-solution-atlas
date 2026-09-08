"""Executable re-arc DSL program for ARC-AGI-2 task f8b3ba0a.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    DOWN,
    ONE,
    THREE,
    UNITY,
    apply,
    astuple,
    canvas,
    colorcount,
    compose,
    compress,
    crop,
    decrement,
    invert,
    lbind,
    merge,
    order,
    palette,
    rbind,
    size,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "f8b3ba0a"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = compress(grid)
    astuple(THREE, ONE)
    x2 = palette(x0)
    x3 = lbind(colorcount, x0)
    x4 = compose(invert, x3)
    x5 = order(x2, x4)
    x6 = rbind(canvas, UNITY)
    x7 = apply(x6, x5)
    x8 = merge(x7)
    x9 = size(x2)
    x10 = decrement(x9)
    x11 = astuple(x10, ONE)
    x12 = crop(x8, DOWN, x11)
    return x12


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
