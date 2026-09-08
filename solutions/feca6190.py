"""Executable re-arc DSL program for ARC-AGI-2 task feca6190.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    UNITY,
    UP_RIGHT,
    ZERO,
    asobject,
    astuple,
    canvas,
    chain,
    compose,
    decrement,
    first,
    flip,
    fork,
    last,
    lbind,
    mapply,
    matcher,
    multiply,
    paint,
    rbind,
    recolor,
    sfilter,
    shoot,
    size,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "feca6190"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = asobject(grid)
    x1 = matcher(first, ZERO)
    x2 = compose(flip, x1)
    x3 = sfilter(x0, x2)
    x4 = size(x3)
    x5 = width(grid)
    x6 = multiply(x5, x4)
    x7 = multiply(UNITY, x6)
    x8 = canvas(ZERO, x7)
    x9 = multiply(x5, x4)
    x10 = decrement(x9)
    x11 = lbind(astuple, x10)
    x12 = rbind(shoot, UP_RIGHT)
    x13 = compose(last, last)
    x14 = chain(x12, x11, x13)
    x15 = fork(recolor, first, x14)
    x16 = mapply(x15, x3)
    x17 = paint(x8, x16)
    return x17


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
