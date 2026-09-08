"""Executable re-arc DSL program for ARC-AGI-2 task bbc9ae5d.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ORIGIN,
    UNITY,
    asobject,
    astuple,
    canvas,
    compose,
    first,
    fork,
    halve,
    index,
    last,
    mapply,
    paint,
    rbind,
    recolor,
    shoot,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "bbc9ae5d"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = index(grid, ORIGIN)
    x1 = width(grid)
    x2 = halve(x1)
    x3 = astuple(x2, x1)
    x4 = canvas(x0, x3)
    x5 = rbind(shoot, UNITY)
    x6 = compose(x5, last)
    x7 = fork(recolor, first, x6)
    x8 = asobject(grid)
    x9 = mapply(x7, x8)
    x10 = paint(x4, x9)
    return x10


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
