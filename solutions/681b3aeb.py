"""Executable re-arc DSL program for ARC-AGI-2 task 681b3aeb.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    ZERO,
    T,
    argmax,
    both,
    canvas,
    color,
    combine,
    compose,
    equality,
    fill,
    first,
    fork,
    height,
    intersection,
    interval,
    invert,
    last,
    lbind,
    matcher,
    multiply,
    normalize,
    objects,
    product,
    shape,
    shift,
    size,
    toindices,
    totuple,
    ulcorner,
    valmax,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "681b3aeb"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, T, T)
    x1 = totuple(x0)
    x2 = first(x1)
    x3 = normalize(x2)
    x4 = last(x1)
    x5 = normalize(x4)
    x6 = color(x3)
    x7 = color(x5)
    x8 = toindices(x3)
    x9 = toindices(x5)
    x10 = fork(multiply, height, width)
    x11 = fork(equality, size, x10)
    x12 = lbind(shift, x8)
    x13 = lbind(shift, x9)
    x14 = compose(x12, first)
    x15 = compose(x13, last)
    x16 = fork(intersection, x14, x15)
    x17 = compose(size, x16)
    x18 = compose(x12, first)
    x19 = compose(x13, last)
    x20 = fork(combine, x18, x19)
    x21 = compose(x11, x20)
    x22 = matcher(x17, ZERO)
    x23 = fork(both, x22, x21)
    x24 = valmax(x1, height)
    x25 = valmax(x1, width)
    x26 = interval(ZERO, x24, ONE)
    x27 = interval(ZERO, x25, ONE)
    x28 = product(x26, x27)
    x29 = product(x28, x28)
    x30 = argmax(x29, x23)
    x31 = first(x30)
    x32 = shift(x8, x31)
    x33 = last(x30)
    x34 = shift(x9, x33)
    x35 = combine(x32, x34)
    x36 = shape(x35)
    x37 = canvas(x7, x36)
    x38 = ulcorner(x35)
    x39 = invert(x38)
    x40 = shift(x32, x39)
    x41 = fill(x37, x6, x40)
    return x41


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
