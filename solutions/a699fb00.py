"""Executable re-arc DSL program for ARC-AGI-2 task a699fb00.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    TWO,
    apply,
    chain,
    delta,
    fork,
    height,
    identity,
    lbind,
    leastcolor,
    merge,
    ofcolor,
    paint,
    rbind,
    recolor,
    vsplit,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "a699fb00"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = leastcolor(grid)
    x1 = height(grid)
    x2 = vsplit(grid, x1)
    x3 = lbind(recolor, TWO)
    x4 = rbind(ofcolor, x0)
    x5 = chain(x3, delta, x4)
    x6 = fork(paint, identity, x5)
    x7 = apply(x6, x2)
    x8 = merge(x7)
    return x8


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
