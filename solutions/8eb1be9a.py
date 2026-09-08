"""Executable re-arc DSL program for ARC-AGI-2 task 8eb1be9a.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ZERO,
    combine,
    compose,
    fgpartition,
    fork,
    height,
    interval,
    invert,
    lbind,
    mapply,
    merge,
    paint,
    shift,
    toivec,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "8eb1be9a"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = fgpartition(grid)
    x1 = merge(x0)
    x2 = height(x1)
    x3 = height(grid)
    x4 = interval(ZERO, x3, x2)
    x5 = lbind(shift, x1)
    x6 = compose(x5, toivec)
    x7 = compose(x6, invert)
    x8 = fork(combine, x6, x7)
    x9 = mapply(x8, x4)
    x10 = paint(grid, x9)
    return x10


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
