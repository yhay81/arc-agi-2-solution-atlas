"""Executable re-arc DSL program for ARC-AGI-2 task 9d9215db.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    FOUR,
    NEG_TWO,
    RIGHT,
    asindices,
    both,
    chain,
    combine,
    compose,
    contained,
    double,
    equality,
    fgpartition,
    first,
    flip,
    fork,
    greater,
    halve,
    hmirror,
    identity,
    increment,
    intersection,
    last,
    lbind,
    mapply,
    matcher,
    merge,
    mostcolor,
    paint,
    power,
    rbind,
    recolor,
    rot90,
    sfilter,
    shift,
    shoot,
    tojvec,
    toobject,
    vmirror,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "9d9215db"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = hmirror(grid)
    x1 = fgpartition(x0)
    x2 = merge(x1)
    x3 = vmirror(grid)
    x4 = fgpartition(x3)
    x5 = merge(x4)
    x6 = hmirror(grid)
    x7 = vmirror(x6)
    x8 = fgpartition(x7)
    x9 = merge(x8)
    x10 = mostcolor(grid)
    x11 = combine(x2, x5)
    x12 = combine(x11, x9)
    x13 = paint(grid, x12)
    x14 = compose(increment, first)
    x15 = fork(greater, last, x14)
    x16 = tojvec(NEG_TWO)
    x17 = rbind(shift, x16)
    x18 = compose(x17, vmirror)
    x19 = rbind(sfilter, x15)
    x20 = compose(x19, asindices)
    x21 = compose(x18, x20)
    x22 = fork(intersection, x20, x21)
    x23 = rbind(shoot, RIGHT)
    x24 = compose(x23, last)
    x25 = matcher(first, x10)
    x26 = compose(flip, x25)
    x27 = rbind(sfilter, x26)
    x28 = compose(double, halve)
    x29 = fork(equality, x28, identity)
    x30 = chain(flip, x29, last)
    x31 = lbind(fork, both)
    x32 = rbind(x31, x30)
    x33 = lbind(fork, recolor)
    x34 = lbind(x33, first)
    x35 = rbind(compose, x24)
    x36 = lbind(rbind, contained)
    x37 = lbind(rbind, sfilter)
    x38 = chain(x34, x35, x37)
    x39 = chain(x38, x32, x36)
    x40 = fork(toobject, x22, identity)
    x41 = compose(x27, x40)
    x42 = compose(x39, x22)
    x43 = fork(mapply, x42, x41)
    x44 = fork(paint, identity, x43)
    x45 = compose(rot90, x44)
    x46 = power(x45, FOUR)
    x47 = x46(x13)
    return x47


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
