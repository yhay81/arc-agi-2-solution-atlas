"""Executable re-arc DSL program for ARC-AGI-2 task b8825c91.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    FOUR,
    NEG_ONE,
    apply,
    cmirror,
    dmirror,
    hmirror,
    lbind,
    maximum,
    pair,
    papply,
    replace,
    vmirror,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "b8825c91"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = replace(grid, FOUR, NEG_ONE)
    x1 = dmirror(x0)
    x2 = papply(pair, x0, x1)
    x3 = lbind(apply, maximum)
    x4 = apply(x3, x2)
    x5 = cmirror(x4)
    x6 = papply(pair, x4, x5)
    x7 = apply(x3, x6)
    x8 = hmirror(x7)
    x9 = papply(pair, x7, x8)
    x10 = apply(x3, x9)
    x11 = vmirror(x10)
    x12 = papply(pair, x11, x10)
    x13 = apply(x3, x12)
    return x13


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
