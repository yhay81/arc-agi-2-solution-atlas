"""Executable re-arc DSL program for ARC-AGI-2 task 4be741c5.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    ORIGIN,
    apply,
    astuple,
    branch,
    crop,
    dedupe,
    dmirror,
    equality,
    first,
    height,
    identity,
    size,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "4be741c5"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = first(grid)
    x1 = dedupe(x0)
    x2 = size(x1)
    x3 = equality(x2, ONE)
    x4 = branch(x3, dmirror, identity)
    x5 = branch(x3, height, width)
    x6 = x5(grid)
    x7 = astuple(ONE, x6)
    x8 = x4(grid)
    x9 = crop(x8, ORIGIN, x7)
    x10 = apply(dedupe, x9)
    x11 = x4(x10)
    return x11


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
