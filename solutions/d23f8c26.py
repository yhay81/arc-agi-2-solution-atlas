"""Executable re-arc DSL program for ARC-AGI-2 task d23f8c26.

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
    asobject,
    both,
    compose,
    fill,
    first,
    flip,
    fork,
    halve,
    last,
    matcher,
    mostcolor,
    sfilter,
    width,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "d23f8c26"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = mostcolor(grid)
    x1 = matcher(first, x0)
    x2 = compose(flip, x1)
    x3 = width(grid)
    x4 = halve(x3)
    x5 = compose(last, last)
    x6 = matcher(x5, x4)
    x7 = compose(flip, x6)
    x8 = asobject(grid)
    x9 = fork(both, x2, x7)
    x10 = sfilter(x8, x9)
    x11 = fill(grid, x0, x10)
    return x11


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
