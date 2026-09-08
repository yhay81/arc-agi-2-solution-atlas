"""Executable re-arc DSL program for ARC-AGI-2 task 5daaa586.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    UNITY,
    F,
    T,
    argmin,
    bordering,
    colorfilter,
    compose,
    connect,
    difference,
    either,
    equality,
    fill,
    first,
    flip,
    fork,
    identity,
    last,
    mapply,
    matcher,
    mfilter,
    mostcolor,
    objects,
    ofcolor,
    outbox,
    palette,
    product,
    rbind,
    sfilter,
    shift,
    subgrid,
    trim,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "5daaa586"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = mostcolor(grid)
    x1 = objects(grid, T, F, F)
    x2 = colorfilter(x1, x0)
    x3 = rbind(bordering, grid)
    x4 = compose(flip, x3)
    x5 = mfilter(x2, x4)
    x6 = outbox(x5)
    x7 = subgrid(x6, grid)
    x8 = trim(x7)
    x9 = palette(x8)
    x10 = matcher(identity, x0)
    x11 = argmin(x9, x10)
    x12 = trim(x7)
    x13 = ofcolor(x12, x11)
    x14 = shift(x13, UNITY)
    x15 = ofcolor(x7, x11)
    x16 = difference(x15, x14)
    x17 = compose(first, first)
    x18 = compose(first, last)
    x19 = fork(equality, x17, x18)
    x20 = compose(last, first)
    x21 = compose(last, last)
    x22 = fork(equality, x20, x21)
    x23 = fork(either, x19, x22)
    x24 = product(x14, x16)
    x25 = sfilter(x24, x23)
    x26 = fork(connect, first, last)
    x27 = mapply(x26, x25)
    x28 = fill(x7, x11, x27)
    return x28


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
