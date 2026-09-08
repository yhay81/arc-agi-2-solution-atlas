"""Executable re-arc DSL program for ARC-AGI-2 task e9afcf9a.

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
    apply,
    asobject,
    astuple,
    chain,
    compose,
    decrement,
    double,
    equality,
    first,
    flip,
    fork,
    halve,
    height,
    identity,
    last,
    lbind,
    paint,
    sfilter,
    subtract,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "e9afcf9a"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = asobject(grid)
    x1 = height(grid)
    x2 = decrement(x1)
    x3 = lbind(subtract, x2)
    x4 = compose(double, halve)
    x5 = fork(equality, identity, x4)
    x6 = compose(last, last)
    x7 = chain(flip, x5, x6)
    x8 = sfilter(x0, x7)
    x9 = chain(x3, first, last)
    x10 = compose(last, last)
    x11 = fork(astuple, x9, x10)
    x12 = fork(astuple, first, x11)
    x13 = apply(x12, x8)
    x14 = paint(grid, x13)
    return x14


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
