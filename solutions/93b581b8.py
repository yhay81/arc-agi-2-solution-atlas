"""Executable re-arc DSL program for ARC-AGI-2 task 93b581b8.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    NEG_TWO,
    TWO,
    TWO_BY_TWO,
    F,
    T,
    apply,
    astuple,
    combine,
    compose,
    fork,
    index,
    lbind,
    llcorner,
    lrcorner,
    mapply,
    objects,
    paint,
    rbind,
    recolor,
    shift,
    toindices,
    ulcorner,
    urcorner,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "93b581b8"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, F, F, T)
    x1 = apply(toindices, x0)
    x2 = lbind(index, grid)
    x3 = compose(x2, lrcorner)
    x4 = astuple(NEG_TWO, NEG_TWO)
    x5 = rbind(shift, x4)
    x6 = fork(recolor, x3, x5)
    x7 = compose(x2, ulcorner)
    x8 = rbind(shift, TWO_BY_TWO)
    x9 = fork(recolor, x7, x8)
    x10 = compose(x2, llcorner)
    x11 = astuple(NEG_TWO, TWO)
    x12 = rbind(shift, x11)
    x13 = fork(recolor, x10, x12)
    x14 = compose(x2, urcorner)
    x15 = astuple(TWO, NEG_TWO)
    x16 = rbind(shift, x15)
    x17 = fork(recolor, x14, x16)
    x18 = fork(combine, x6, x9)
    x19 = fork(combine, x13, x17)
    x20 = fork(combine, x18, x19)
    x21 = mapply(x20, x1)
    x22 = paint(grid, x21)
    return x22


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
