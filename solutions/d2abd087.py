"""Executable re-arc DSL program for ARC-AGI-2 task d2abd087.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    SIX,
    TWO,
    F,
    T,
    compose,
    fill,
    flip,
    matcher,
    mfilter,
    objects,
    size,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "d2abd087"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, T)
    x1 = matcher(size, SIX)
    x2 = compose(flip, x1)
    x3 = mfilter(x0, x1)
    x4 = mfilter(x0, x2)
    x5 = fill(grid, TWO, x3)
    x6 = fill(x5, ONE, x4)
    return x6


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
