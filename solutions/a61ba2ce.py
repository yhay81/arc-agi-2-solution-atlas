"""Executable re-arc DSL program for ARC-AGI-2 task a61ba2ce.

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
    add,
    astuple,
    canvas,
    compose,
    contained,
    extract,
    fgpartition,
    flip,
    fork,
    height,
    llcorner,
    lrcorner,
    mostcolor,
    normalize,
    paint,
    shape,
    shift,
    subtract,
    toindices,
    toivec,
    tojvec,
    ulcorner,
    urcorner,
    width,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "a61ba2ce"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = fgpartition(grid)
    x1 = fork(contained, lrcorner, toindices)
    x2 = compose(flip, x1)
    x3 = extract(x0, x2)
    x4 = fork(contained, llcorner, toindices)
    x5 = compose(flip, x4)
    x6 = extract(x0, x5)
    x7 = fork(contained, urcorner, toindices)
    x8 = compose(flip, x7)
    x9 = extract(x0, x8)
    x10 = fork(contained, ulcorner, toindices)
    x11 = compose(flip, x10)
    x12 = extract(x0, x11)
    x13 = height(x3)
    x14 = height(x9)
    x15 = add(x13, x14)
    x16 = width(x3)
    x17 = width(x6)
    x18 = add(x16, x17)
    x19 = astuple(x15, x18)
    x20 = mostcolor(grid)
    x21 = canvas(x20, x19)
    x22 = normalize(x3)
    x23 = paint(x21, x22)
    x24 = normalize(x6)
    x25 = width(x6)
    x26 = subtract(x18, x25)
    x27 = tojvec(x26)
    x28 = shift(x24, x27)
    x29 = paint(x23, x28)
    x30 = normalize(x9)
    x31 = height(x9)
    x32 = subtract(x15, x31)
    x33 = toivec(x32)
    x34 = shift(x30, x33)
    x35 = paint(x29, x34)
    x36 = normalize(x12)
    x37 = shape(x12)
    x38 = subtract(x19, x37)
    x39 = shift(x36, x38)
    x40 = paint(x35, x39)
    return x40


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
