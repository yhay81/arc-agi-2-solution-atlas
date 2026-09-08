"""Executable re-arc DSL program for ARC-AGI-2 task 496994bd.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    TWO,
    apply,
    asobject,
    branch,
    compose,
    contained,
    first,
    flip,
    hmirror,
    matcher,
    mostcolor,
    numcolors,
    paint,
    sfilter,
    vmirror,
    vsplit,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "496994bd"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = mostcolor(grid)
    x1 = vsplit(grid, TWO)
    x2 = apply(numcolors, x1)
    x3 = contained(ONE, x2)
    x4 = branch(x3, hmirror, vmirror)
    x5 = x4(grid)
    x6 = asobject(x5)
    x7 = matcher(first, x0)
    x8 = compose(flip, x7)
    x9 = sfilter(x6, x8)
    x10 = paint(grid, x9)
    return x10


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
