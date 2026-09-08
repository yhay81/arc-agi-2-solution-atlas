"""Executable re-arc DSL program for ARC-AGI-2 task f25ffba3.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    asobject,
    bottomhalf,
    branch,
    compose,
    dmirror,
    either,
    equality,
    first,
    flip,
    hmirror,
    identity,
    matcher,
    mostcolor,
    numcolors,
    paint,
    sfilter,
    tophalf,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "f25ffba3"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = tophalf(grid)
    x1 = numcolors(x0)
    x2 = equality(x1, ONE)
    x3 = bottomhalf(grid)
    x4 = numcolors(x3)
    x5 = equality(x4, ONE)
    x6 = either(x2, x5)
    x7 = branch(x6, identity, dmirror)
    x8 = x7(grid)
    x9 = asobject(x8)
    x10 = hmirror(x9)
    x11 = mostcolor(grid)
    x12 = matcher(first, x11)
    x13 = compose(flip, x12)
    x14 = sfilter(x10, x13)
    x15 = paint(x8, x14)
    x16 = x7(x15)
    return x16


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
