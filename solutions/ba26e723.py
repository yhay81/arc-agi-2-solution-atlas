"""Executable re-arc DSL program for ARC-AGI-2 task ba26e723.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    SIX,
    THREE,
    ZERO,
    asobject,
    compose,
    divide,
    equality,
    fill,
    first,
    flip,
    fork,
    identity,
    last,
    matcher,
    multiply,
    rbind,
    sfilter,
    toindices,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "ba26e723"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = asobject(grid)
    x1 = matcher(first, ZERO)
    x2 = compose(flip, x1)
    x3 = sfilter(x0, x2)
    x4 = rbind(multiply, THREE)
    x5 = rbind(divide, THREE)
    x6 = compose(x4, x5)
    x7 = fork(equality, identity, x6)
    x8 = toindices(x3)
    x9 = compose(x7, last)
    x10 = sfilter(x8, x9)
    x11 = fill(grid, SIX, x10)
    return x11


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
