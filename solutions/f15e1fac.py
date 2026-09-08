"""Executable re-arc DSL program for ARC-AGI-2 task f15e1fac.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    TWO,
    ZERO,
    add,
    apply,
    astuple,
    branch,
    chain,
    cmirror,
    combine,
    compose,
    connect,
    decrement,
    dmirror,
    equality,
    extract,
    fill,
    first,
    fork,
    hmirror,
    identity,
    initset,
    insert,
    interval,
    last,
    lbind,
    lowermost,
    mapply,
    matcher,
    mostcolor,
    ofcolor,
    order,
    other,
    pair,
    palette,
    rapply,
    rbind,
    remove,
    rightmost,
    size,
    vmirror,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "f15e1fac"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = rbind(ofcolor, TWO)
    x1 = compose(lowermost, x0)
    x2 = matcher(x1, ZERO)
    x3 = astuple(identity, dmirror)
    x4 = astuple(cmirror, hmirror)
    x5 = combine(x3, x4)
    x6 = rbind(rapply, grid)
    x7 = compose(first, x6)
    x8 = chain(x2, x7, initset)
    x9 = extract(x5, x8)
    x10 = x9(grid)
    x11 = mostcolor(grid)
    x12 = palette(grid)
    x13 = remove(x11, x12)
    x14 = other(x13, TWO)
    x15 = ofcolor(x10, x14)
    x16 = rightmost(x15)
    x17 = equality(x16, ZERO)
    x18 = branch(x17, identity, vmirror)
    x19 = x18(x10)
    x20 = ofcolor(x19, x14)
    x21 = ofcolor(x19, TWO)
    x22 = apply(last, x21)
    x23 = insert(ZERO, x22)
    x24 = width(x19)
    x25 = insert(x24, x23)
    x26 = order(x25, identity)
    x27 = last(x26)
    x28 = remove(x27, x26)
    x29 = first(x26)
    x30 = remove(x29, x26)
    x31 = pair(x28, x30)
    x32 = size(x28)
    x33 = interval(ZERO, x32, ONE)
    x34 = pair(x33, x31)
    x35 = lbind(fork, connect)
    x36 = compose(first, last)
    x37 = chain(decrement, last, last)
    x38 = lbind(lbind, add)
    x39 = compose(x38, first)
    x40 = lbind(rbind, astuple)
    x41 = rbind(chain, first)
    x42 = compose(x40, x36)
    x43 = compose(x40, x37)
    x44 = fork(x41, x42, x39)
    x45 = fork(x41, x43, x39)
    x46 = fork(x35, x44, x45)
    x47 = rbind(mapply, x20)
    x48 = compose(x47, x46)
    x49 = mapply(x48, x34)
    x50 = fill(x19, x14, x49)
    x51 = x18(x50)
    x52 = x9(x51)
    return x52


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
