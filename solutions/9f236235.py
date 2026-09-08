"""Executable re-arc DSL program for ARC-AGI-2 task 9f236235.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    F,
    T,
    apply,
    canvas,
    chain,
    color,
    compose,
    frontiers,
    hconcat,
    identity,
    lbind,
    leftmost,
    matcher,
    merge,
    objects,
    order,
    rbind,
    sfilter,
    shape,
    uppermost,
    vmirror,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "9f236235"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = frontiers(grid)
    x1 = merge(x0)
    x2 = color(x1)
    x3 = shape(grid)
    x4 = canvas(x2, x3)
    x5 = hconcat(grid, x4)
    x6 = objects(x5, T, F, T)
    x7 = apply(uppermost, x6)
    x8 = order(x7, identity)
    x9 = lbind(sfilter, x6)
    x10 = lbind(matcher, uppermost)
    x11 = compose(x9, x10)
    x12 = lbind(apply, color)
    x13 = rbind(order, leftmost)
    x14 = chain(x12, x13, x11)
    x15 = apply(x14, x8)
    x16 = vmirror(x15)
    return x16


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
