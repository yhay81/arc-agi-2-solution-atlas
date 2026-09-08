"""Executable re-arc DSL program for ARC-AGI-2 task 995c5fa3.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    DOWN,
    EIGHT,
    FIVE,
    FOUR,
    NEG_ONE,
    ONE,
    THREE,
    TWO,
    ZERO,
    add,
    apply,
    asindices,
    astuple,
    canvas,
    chain,
    compose,
    divide,
    either,
    equality,
    flip,
    fork,
    hmirror,
    identity,
    increment,
    index,
    interval,
    lbind,
    matcher,
    multiply,
    numcolors,
    rbind,
    repeat,
    shift,
    tojvec,
    toobject,
    ulcorner,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "995c5fa3"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = width(grid)
    x1 = increment(x0)
    x2 = divide(x1, FIVE)
    x3 = astuple(FOUR, FOUR)
    x4 = canvas(NEG_ONE, x3)
    x5 = asindices(x4)
    x6 = rbind(toobject, grid)
    x7 = lbind(shift, x5)
    x8 = compose(x6, x7)
    x9 = multiply(x2, FIVE)
    x10 = interval(ZERO, x9, FIVE)
    x11 = apply(tojvec, x10)
    x12 = apply(x8, x11)
    x13 = matcher(numcolors, ONE)
    x14 = fork(equality, identity, hmirror)
    x15 = compose(flip, x14)
    x16 = lbind(index, grid)
    x17 = compose(x16, ulcorner)
    x18 = lbind(add, DOWN)
    x19 = chain(x16, x18, ulcorner)
    x20 = fork(equality, x17, x19)
    x21 = compose(flip, x20)
    x22 = fork(either, x13, x15)
    x23 = fork(either, x22, x21)
    x24 = compose(flip, x23)
    x25 = lbind(multiply, TWO)
    x26 = compose(x25, x13)
    x27 = lbind(multiply, FOUR)
    x28 = compose(x27, x15)
    x29 = fork(add, x26, x28)
    x30 = lbind(multiply, THREE)
    x31 = compose(x30, x21)
    x32 = lbind(multiply, EIGHT)
    x33 = compose(x32, x24)
    x34 = fork(add, x31, x33)
    x35 = fork(add, x29, x34)
    x36 = apply(x35, x12)
    x37 = rbind(repeat, x2)
    x38 = apply(x37, x36)
    return x38


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
