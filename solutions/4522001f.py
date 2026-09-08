"""Executable re-arc DSL program for ARC-AGI-2 task 4522001f.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    FOUR,
    ONE,
    ORIGIN,
    THREE,
    F,
    T,
    adjacent,
    apply,
    asobject,
    backdrop,
    canvas,
    chain,
    combine,
    compose,
    decrement,
    delta,
    dneighbors,
    double,
    extract,
    fill,
    first,
    fork,
    identity,
    ineighbors,
    lbind,
    mapply,
    matcher,
    merge,
    mostcolor,
    multiply,
    normalize,
    objects,
    paint,
    rbind,
    sfilter,
    shape,
    shift,
    subtract,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "4522001f"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = shape(grid)
    x1 = multiply(THREE, x0)
    x2 = mostcolor(grid)
    x3 = canvas(x2, x1)
    x4 = objects(grid, F, F, T)
    x5 = merge(x4)
    x6 = mostcolor(x5)
    x7 = first(x4)
    x8 = matcher(first, x6)
    x9 = sfilter(x7, x8)
    x10 = normalize(x9)
    x11 = delta(x10)
    x12 = first(x11)
    x13 = subtract(ONE, x12)
    x14 = asobject(grid)
    x15 = shape(grid)
    x16 = double(x15)
    x17 = multiply(x13, x16)
    x18 = shift(x14, x17)
    x19 = paint(x3, x18)
    x20 = objects(x19, F, F, T)
    x21 = lbind(mapply, dneighbors)
    x22 = matcher(first, x6)
    x23 = rbind(sfilter, x22)
    x24 = chain(x21, delta, x23)
    x25 = ineighbors(ORIGIN)
    x26 = apply(double, x25)
    x27 = rbind(apply, x26)
    x28 = lbind(lbind, shift)
    x29 = compose(x27, x28)
    x30 = lbind(rbind, adjacent)
    x31 = compose(x30, x24)
    x32 = fork(extract, x29, x31)
    x33 = fork(combine, identity, x32)
    x34 = compose(backdrop, x33)
    x35 = double(x12)
    x36 = decrement(x35)
    x37 = multiply(x36, FOUR)
    x38 = rbind(shift, x37)
    x39 = compose(x38, x34)
    x40 = fork(combine, x34, x39)
    x41 = mapply(x40, x20)
    x42 = fill(x19, x6, x41)
    return x42


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
