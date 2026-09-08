"""Executable re-arc DSL program for ARC-AGI-2 task cbded52d.

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
    apply,
    argmax,
    both,
    chain,
    color,
    colorcount,
    compose,
    connect,
    divide,
    either,
    equality,
    first,
    fork,
    frontiers,
    height,
    hline,
    identity,
    increment,
    last,
    lbind,
    leftmost,
    mapply,
    merge,
    multiply,
    ofcolor,
    paint,
    palette,
    product,
    rbind,
    recolor,
    remove,
    sfilter,
    size,
    subtract,
    uppermost,
    vline,
    width,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "cbded52d"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = frontiers(grid)
    x1 = merge(x0)
    x2 = color(x1)
    x3 = palette(grid)
    x4 = remove(x2, x3)
    x5 = lbind(colorcount, grid)
    x6 = argmax(x4, x5)
    x7 = remove(x6, x4)
    x8 = height(grid)
    x9 = increment(x8)
    x10 = frontiers(grid)
    x11 = sfilter(x10, hline)
    x12 = size(x11)
    x13 = increment(x12)
    x14 = divide(x9, x13)
    x15 = width(grid)
    x16 = increment(x15)
    x17 = frontiers(grid)
    x18 = sfilter(x17, vline)
    x19 = size(x18)
    x20 = increment(x19)
    x21 = divide(x16, x20)
    x22 = rbind(multiply, x14)
    x23 = rbind(divide, x14)
    x24 = compose(x22, x23)
    x25 = fork(equality, identity, x24)
    x26 = rbind(multiply, x21)
    x27 = rbind(divide, x21)
    x28 = compose(x26, x27)
    x29 = fork(equality, identity, x28)
    x30 = lbind(fork, both)
    x31 = rbind(compose, first)
    x32 = lbind(compose, x25)
    x33 = lbind(rbind, subtract)
    x34 = compose(x33, uppermost)
    x35 = chain(x31, x32, x34)
    x36 = rbind(compose, last)
    x37 = lbind(compose, x29)
    x38 = lbind(rbind, subtract)
    x39 = compose(x38, leftmost)
    x40 = chain(x36, x37, x39)
    x41 = fork(x30, x35, x40)
    x42 = fork(sfilter, identity, x41)
    x43 = fork(connect, first, last)
    x44 = lbind(apply, x43)
    x45 = lbind(ofcolor, grid)
    x46 = fork(product, x45, x45)
    x47 = fork(either, vline, hline)
    x48 = rbind(sfilter, x47)
    x49 = chain(x48, x44, x46)
    x50 = lbind(mapply, x42)
    x51 = compose(x50, x49)
    x52 = fork(recolor, identity, x51)
    x53 = mapply(x52, x7)
    x54 = paint(grid, x53)
    return x54


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
