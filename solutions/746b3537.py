"""Executable re-arc DSL program for ARC-AGI-2 task 746b3537.

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
    branch,
    color,
    dedupe,
    dmirror,
    equality,
    first,
    identity,
    leftmost,
    objects,
    order,
    repeat,
    size,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "746b3537"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = first(grid)
    x1 = dedupe(x0)
    x2 = size(x1)
    x3 = equality(ONE, x2)
    x4 = branch(x3, dmirror, identity)
    x5 = x4(grid)
    x6 = objects(x5, T, F, F)
    x7 = order(x6, leftmost)
    x8 = apply(color, x7)
    x9 = repeat(x8, ONE)
    x10 = x4(x9)
    return x10


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
