"""Executable re-arc DSL program for ARC-AGI-2 task bc1d5164.

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
    asindices,
    astuple,
    canvas,
    chain,
    combine,
    decrement,
    fill,
    first,
    frontiers,
    halve,
    height,
    increment,
    matcher,
    merge,
    mostcolor,
    normalize,
    other,
    palette,
    rbind,
    sfilter,
    shift,
    toindices,
    toivec,
    tojvec,
    toobject,
    width,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "bc1d5164"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = height(grid)
    x1 = halve(x0)
    x2 = increment(x1)
    x3 = width(grid)
    x4 = halve(x3)
    x5 = frontiers(grid)
    x6 = merge(x5)
    x7 = mostcolor(x6)
    x8 = astuple(x2, x4)
    x9 = canvas(x7, x8)
    x10 = asindices(x9)
    x11 = toobject(x10, grid)
    x12 = increment(x4)
    x13 = tojvec(x12)
    x14 = shift(x10, x13)
    x15 = toobject(x14, grid)
    x16 = decrement(x2)
    x17 = toivec(x16)
    x18 = shift(x10, x17)
    x19 = toobject(x18, grid)
    x20 = decrement(x2)
    x21 = increment(x4)
    x22 = astuple(x20, x21)
    x23 = shift(x10, x22)
    x24 = toobject(x23, grid)
    x25 = palette(grid)
    x26 = other(x25, x7)
    x27 = matcher(first, x26)
    x28 = rbind(sfilter, x27)
    x29 = chain(toindices, x28, normalize)
    x30 = x29(x11)
    x31 = x29(x15)
    x32 = x29(x19)
    x33 = x29(x24)
    x34 = combine(x30, x31)
    x35 = combine(x32, x33)
    x36 = combine(x34, x35)
    x37 = fill(x9, x26, x36)
    return x37


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
