"""Executable re-arc DSL program for ARC-AGI-2 task a5f85a15.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    FOUR,
    ORIGIN,
    UNITY,
    ZERO,
    apply,
    compose,
    contained,
    double,
    fill,
    identity,
    increment,
    lbind,
    leastcolor,
    mapply,
    ofcolor,
    order,
    sfilter,
    shift,
    shoot,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "a5f85a15"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = leastcolor(grid)
    x1 = ofcolor(grid, x0)
    x2 = compose(increment, double)
    x3 = shoot(ORIGIN, UNITY)
    x4 = apply(x2, x3)
    x5 = order(x4, identity)
    x6 = lbind(contained, ZERO)
    x7 = sfilter(x1, x6)
    x8 = lbind(shift, x5)
    x9 = mapply(x8, x7)
    x10 = fill(grid, FOUR, x9)
    return x10


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
