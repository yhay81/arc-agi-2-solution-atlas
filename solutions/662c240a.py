"""Executable re-arc DSL program for ARC-AGI-2 task 662c240a.

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
    branch,
    compose,
    divide,
    dmirror,
    equality,
    extract,
    flip,
    fork,
    hsplit,
    identity,
    maximum,
    minimum,
    portrait,
    shape,
    vsplit,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "662c240a"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = portrait(grid)
    x1 = branch(x0, vsplit, hsplit)
    x2 = shape(grid)
    x3 = maximum(x2)
    x4 = minimum(x2)
    x5 = divide(x3, x4)
    x6 = x1(grid, x5)
    x7 = fork(equality, identity, dmirror)
    x8 = compose(flip, x7)
    x9 = extract(x6, x8)
    return x9


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
