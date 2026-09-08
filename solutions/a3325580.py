"""Executable re-arc DSL program for ARC-AGI-2 task a3325580.

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
    astuple,
    canvas,
    color,
    dmirror,
    leftmost,
    merge,
    objects,
    order,
    rbind,
    size,
    sizefilter,
    valmax,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "a3325580"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, T)
    x1 = valmax(x0, size)
    x2 = sizefilter(x0, x1)
    x3 = order(x2, leftmost)
    x4 = apply(color, x3)
    x5 = astuple(ONE, x1)
    x6 = rbind(canvas, x5)
    x7 = apply(x6, x4)
    x8 = merge(x7)
    x9 = dmirror(x8)
    return x9


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
