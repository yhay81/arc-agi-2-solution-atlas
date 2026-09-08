"""Executable re-arc DSL program for ARC-AGI-2 task 6d0160f0.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    FOUR,
    NEG_ONE,
    F,
    T,
    argmax,
    canvas,
    center,
    chain,
    colorcount,
    compose,
    contained,
    extract,
    fill,
    first,
    flip,
    frontiers,
    hconcat,
    increment,
    lbind,
    matcher,
    merge,
    mostcolor,
    multiply,
    normalize,
    objects,
    paint,
    palette,
    rbind,
    remove,
    sfilter,
    shape,
    shift,
    size,
    valmax,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "6d0160f0"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = frontiers(grid)
    x1 = merge(x0)
    x2 = mostcolor(x1)
    x3 = shape(grid)
    x4 = canvas(NEG_ONE, x3)
    x5 = hconcat(grid, x4)
    x6 = fill(x5, NEG_ONE, x1)
    x7 = objects(x6, F, F, T)
    x8 = lbind(contained, FOUR)
    x9 = compose(x8, palette)
    x10 = extract(x7, x9)
    x11 = lbind(sfilter, x7)
    x12 = compose(size, x11)
    x13 = rbind(compose, palette)
    x14 = lbind(lbind, contained)
    x15 = chain(x12, x13, x14)
    x16 = merge(x7)
    x17 = palette(grid)
    x18 = remove(x2, x17)
    x19 = valmax(x18, x15)
    x20 = matcher(x15, x19)
    x21 = sfilter(x18, x20)
    x22 = lbind(colorcount, x16)
    x23 = argmax(x21, x22)
    x24 = shape(grid)
    x25 = canvas(x23, x24)
    x26 = paint(x25, x1)
    x27 = normalize(x10)
    x28 = matcher(first, x2)
    x29 = compose(flip, x28)
    x30 = sfilter(x27, x29)
    x31 = shape(x27)
    x32 = increment(x31)
    x33 = matcher(first, FOUR)
    x34 = sfilter(x27, x33)
    x35 = center(x34)
    x36 = multiply(x32, x35)
    x37 = shift(x30, x36)
    x38 = paint(x26, x37)
    return x38


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
