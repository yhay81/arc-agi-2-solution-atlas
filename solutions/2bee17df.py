"""Executable re-arc DSL program for ARC-AGI-2 task 2bee17df.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    THREE,
    UNITY,
    apply,
    branch,
    combine,
    compose,
    dedupe,
    dmirror,
    fill,
    first,
    fork,
    identity,
    initset,
    lbind,
    matcher,
    mostcolor,
    ofcolor,
    rapply,
    rbind,
    repeat,
    shift,
    size,
    trim,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "2bee17df"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = trim(grid)
    x1 = mostcolor(x0)
    x2 = repeat(x1, ONE)
    x3 = lbind(repeat, THREE)
    x4 = compose(x3, size)
    x5 = matcher(dedupe, x2)
    x6 = rbind(branch, identity)
    x7 = rbind(x6, x4)
    x8 = compose(x7, x5)
    x9 = compose(initset, x8)
    x10 = fork(rapply, x9, identity)
    x11 = compose(first, x10)
    x12 = apply(x11, x0)
    x13 = dmirror(x0)
    x14 = apply(x11, x13)
    x15 = dmirror(x14)
    x16 = ofcolor(x12, THREE)
    x17 = ofcolor(x15, THREE)
    x18 = combine(x16, x17)
    x19 = shift(x18, UNITY)
    x20 = fill(grid, THREE, x19)
    return x20


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
