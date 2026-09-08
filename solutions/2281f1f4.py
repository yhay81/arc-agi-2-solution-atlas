"""Executable re-arc DSL program for ARC-AGI-2 task 2281f1f4.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    TWO,
    apply,
    argmax,
    asindices,
    chain,
    compose,
    corners,
    difference,
    either,
    fill,
    first,
    fork,
    initset,
    last,
    lbind,
    leastcolor,
    matcher,
    mostcolor,
    ofcolor,
    product,
    sfilter,
    size,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "2281f1f4"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = leastcolor(grid)
    x1 = ofcolor(grid, x0)
    x2 = apply(first, x1)
    x3 = apply(last, x1)
    x4 = product(x2, x3)
    x5 = difference(x4, x1)
    x6 = fill(grid, TWO, x5)
    x7 = lbind(fork, either)
    x8 = lbind(matcher, first)
    x9 = compose(x8, first)
    x10 = lbind(matcher, last)
    x11 = compose(x10, last)
    x12 = fork(x7, x9, x11)
    x13 = lbind(sfilter, x1)
    x14 = chain(size, x13, x12)
    x15 = asindices(grid)
    x16 = corners(x15)
    x17 = argmax(x16, x14)
    x18 = mostcolor(grid)
    x19 = initset(x17)
    x20 = fill(x6, x18, x19)
    return x20


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
