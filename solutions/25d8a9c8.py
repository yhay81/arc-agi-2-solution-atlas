"""Executable re-arc DSL program for ARC-AGI-2 task 25d8a9c8.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    FIVE,
    ONE,
    ZERO,
    apply,
    branch,
    compose,
    dedupe,
    matcher,
    rbind,
    repeat,
    size,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "25d8a9c8"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = width(grid)
    x1 = rbind(branch, ZERO)
    x2 = rbind(x1, FIVE)
    x3 = compose(size, dedupe)
    x4 = matcher(x3, ONE)
    x5 = compose(x2, x4)
    x6 = rbind(repeat, x0)
    x7 = compose(x6, x5)
    x8 = apply(x7, grid)
    return x8


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
