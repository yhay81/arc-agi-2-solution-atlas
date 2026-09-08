"""Executable re-arc DSL program for ARC-AGI-2 task a87f7484.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    TEN,
    THREE,
    TWO,
    add,
    apply,
    argmax,
    argmin,
    chain,
    combine,
    compose,
    contained,
    dedupe,
    equality,
    fork,
    halve,
    height,
    hsplit,
    increment,
    interval,
    lbind,
    matcher,
    mostcommon,
    multiply,
    palette,
    partition,
    positive,
    rbind,
    sfilter,
    shape,
    size,
    toindices,
    vsplit,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "a87f7484"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = height(grid)
    x1 = halve(x0)
    x2 = increment(x1)
    x3 = interval(THREE, x2, ONE)
    x4 = width(grid)
    x5 = halve(x4)
    x6 = increment(x5)
    x7 = interval(THREE, x6, ONE)
    x8 = palette(grid)
    x9 = lbind(apply, toindices)
    x10 = compose(x9, partition)
    x11 = rbind(compose, palette)
    x12 = lbind(lbind, contained)
    x13 = compose(x11, x12)
    x14 = lbind(chain, size)
    x15 = rbind(x14, x13)
    x16 = lbind(lbind, sfilter)
    x17 = compose(x15, x16)
    x18 = compose(positive, size)
    x19 = lbind(sfilter, x8)
    x20 = fork(matcher, x17, size)
    x21 = chain(x18, x19, x20)
    x22 = lbind(apply, shape)
    x23 = chain(size, dedupe, x22)
    x24 = matcher(x23, ONE)
    x25 = lbind(apply, x10)
    x26 = chain(size, dedupe, x25)
    x27 = matcher(x26, TWO)
    x28 = compose(size, dedupe)
    x29 = fork(equality, size, x28)
    x30 = fork(add, x21, x24)
    x31 = fork(add, x27, x29)
    x32 = fork(add, x30, x31)
    x33 = multiply(TEN, TEN)
    x34 = lbind(multiply, x33)
    x35 = compose(x34, x32)
    x36 = fork(add, x35, size)
    x37 = lbind(vsplit, grid)
    x38 = apply(x37, x3)
    x39 = lbind(hsplit, grid)
    x40 = apply(x39, x7)
    x41 = combine(x38, x40)
    x42 = argmax(x41, x36)
    x43 = apply(x10, x42)
    x44 = mostcommon(x43)
    x45 = matcher(x10, x44)
    x46 = argmin(x42, x45)
    return x46


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
