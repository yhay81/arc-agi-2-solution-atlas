"""Executable re-arc DSL program for ARC-AGI-2 task 890034e9.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    NEG_UNITY,
    TWO,
    ZERO,
    F,
    T,
    apply,
    box,
    chain,
    color,
    equality,
    fill,
    fork,
    greater,
    inbox,
    lbind,
    leastcommon,
    mapply,
    minimum,
    normalize,
    objects,
    occurrences,
    ofcolor,
    rbind,
    recolor,
    sfilter,
    shape,
    shift,
    toindices,
    totuple,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "890034e9"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = rbind(greater, TWO)
    x1 = chain(x0, minimum, shape)
    x2 = objects(grid, T, F, F)
    x3 = sfilter(x2, x1)
    x4 = fork(equality, toindices, box)
    x5 = sfilter(x3, x4)
    x6 = totuple(x5)
    x7 = apply(color, x6)
    x8 = leastcommon(x7)
    x9 = ofcolor(grid, x8)
    x10 = inbox(x9)
    x11 = recolor(ZERO, x10)
    x12 = occurrences(grid, x11)
    x13 = normalize(x9)
    x14 = shift(x13, NEG_UNITY)
    x15 = lbind(shift, x14)
    x16 = mapply(x15, x12)
    x17 = fill(grid, x8, x16)
    return x17


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
