"""Executable re-arc DSL program for ARC-AGI-2 task 6cdd2623.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ZERO,
    argmax,
    asindices,
    both,
    box,
    canvas,
    chain,
    color,
    compose,
    connect,
    difference,
    either,
    fill,
    flip,
    fork,
    hline,
    matcher,
    mfilter,
    mostcolor,
    partition,
    prapply,
    rbind,
    sfilter,
    shape,
    size,
    toindices,
    vline,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "6cdd2623"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = asindices(grid)
    x1 = box(x0)
    x2 = rbind(difference, x1)
    x3 = chain(size, x2, toindices)
    x4 = matcher(x3, ZERO)
    x5 = partition(grid)
    x6 = sfilter(x5, x4)
    x7 = argmax(x6, size)
    x8 = color(x7)
    x9 = toindices(x7)
    x10 = fork(either, hline, vline)
    x11 = prapply(connect, x9, x9)
    x12 = compose(flip, x4)
    x13 = fork(both, x12, x10)
    x14 = mfilter(x11, x13)
    x15 = mostcolor(grid)
    x16 = shape(grid)
    x17 = canvas(x15, x16)
    x18 = fill(x17, x8, x14)
    return x18


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
