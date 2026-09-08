"""Executable re-arc DSL program for ARC-AGI-2 task 9af7a82c.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    ZERO,
    apply,
    astuple,
    canvas,
    chain,
    cmirror,
    color,
    compose,
    fork,
    lbind,
    merge,
    order,
    partition,
    rbind,
    size,
    subtract,
    valmax,
    vconcat,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "9af7a82c"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = partition(grid)
    x1 = order(x0, size)
    x2 = valmax(x0, size)
    x3 = rbind(astuple, ONE)
    x4 = lbind(subtract, x2)
    x5 = compose(x3, size)
    x6 = chain(x3, x4, size)
    x7 = fork(canvas, color, x5)
    x8 = lbind(canvas, ZERO)
    x9 = compose(x8, x6)
    x10 = fork(vconcat, x7, x9)
    x11 = compose(cmirror, x10)
    x12 = apply(x11, x1)
    x13 = merge(x12)
    x14 = cmirror(x13)
    return x14


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
