"""Executable re-arc DSL program for ARC-AGI-2 task 80af3007.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    ZERO,
    apply,
    argmin,
    canvas,
    chain,
    color,
    compose,
    divide,
    equality,
    extract,
    fill,
    first,
    fork,
    height,
    identity,
    interval,
    last,
    lbind,
    mapply,
    matcher,
    multiply,
    ofcolor,
    other,
    pair,
    palette,
    partition,
    rbind,
    sfilter,
    shape,
    shift,
    subgrid,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "80af3007"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = partition(grid)
    x1 = fork(multiply, height, width)
    x2 = argmin(x0, x1)
    x3 = color(x2)
    x4 = palette(grid)
    x5 = other(x4, x3)
    x6 = subgrid(x2, grid)
    x7 = fork(multiply, identity, identity)
    x8 = width(x6)
    x9 = matcher(x7, x8)
    x10 = fork(multiply, identity, identity)
    x11 = height(x6)
    x12 = matcher(x10, x11)
    x13 = width(x6)
    x14 = interval(ONE, x13, ONE)
    x15 = extract(x14, x9)
    x16 = height(x6)
    x17 = interval(ONE, x16, ONE)
    x18 = extract(x17, x12)
    x19 = width(x6)
    x20 = interval(ZERO, x19, ONE)
    x21 = height(x6)
    x22 = interval(ZERO, x21, ONE)
    x23 = rbind(multiply, x15)
    x24 = rbind(divide, x15)
    x25 = compose(x23, x24)
    x26 = fork(equality, identity, x25)
    x27 = compose(x26, last)
    x28 = rbind(multiply, x18)
    x29 = rbind(divide, x18)
    x30 = compose(x28, x29)
    x31 = fork(equality, identity, x30)
    x32 = compose(x31, last)
    x33 = lbind(apply, first)
    x34 = rbind(sfilter, x27)
    x35 = rbind(pair, x20)
    x36 = chain(x33, x34, x35)
    x37 = pair(x6, x22)
    x38 = sfilter(x37, x32)
    x39 = apply(first, x38)
    x40 = apply(x36, x39)
    x41 = shape(x40)
    x42 = multiply(x41, x41)
    x43 = canvas(x5, x42)
    x44 = ofcolor(x40, x3)
    x45 = rbind(multiply, x41)
    x46 = apply(x45, x44)
    x47 = lbind(shift, x44)
    x48 = mapply(x47, x46)
    x49 = fill(x43, x3, x48)
    return x49


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
