"""Executable re-arc DSL program for ARC-AGI-2 task ff805c23.

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
    argmin,
    asobject,
    both,
    chain,
    cmirror,
    colorcount,
    compose,
    dmirror,
    equality,
    first,
    flip,
    fork,
    hmirror,
    identity,
    initset,
    lbind,
    matcher,
    ofcolor,
    paint,
    palette,
    rapply,
    rbind,
    sfilter,
    subgrid,
    vmirror,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "ff805c23"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = palette(grid)
    x1 = lbind(rbind, sfilter)
    x2 = lbind(compose, flip)
    x3 = lbind(matcher, first)
    x4 = chain(x1, x2, x3)
    x5 = lbind(paint, grid)
    x6 = rbind(compose, asobject)
    x7 = dmirror(grid)
    x8 = rbind(rapply, x7)
    x9 = chain(first, x8, initset)
    x10 = chain(x9, x6, x4)
    x11 = compose(x5, x10)
    x12 = compose(x6, x4)
    x13 = compose(cmirror, x11)
    x14 = compose(initset, x12)
    x15 = fork(rapply, x14, x13)
    x16 = compose(first, x15)
    x17 = fork(paint, x11, x16)
    x18 = chain(initset, x6, x4)
    x19 = compose(hmirror, x17)
    x20 = fork(rapply, x18, x19)
    x21 = compose(first, x20)
    x22 = fork(paint, x17, x21)
    x23 = chain(initset, x6, x4)
    x24 = compose(vmirror, x22)
    x25 = fork(rapply, x23, x24)
    x26 = compose(first, x25)
    x27 = fork(paint, x22, x26)
    x28 = fork(equality, identity, hmirror)
    x29 = fork(equality, identity, vmirror)
    x30 = fork(equality, identity, cmirror)
    x31 = fork(equality, identity, dmirror)
    x32 = fork(both, x28, x29)
    x33 = fork(both, x30, x31)
    x34 = fork(both, x32, x33)
    x35 = compose(x34, x27)
    x36 = sfilter(x0, x35)
    x37 = lbind(colorcount, grid)
    x38 = argmin(x36, x37)
    x39 = x27(x38)
    x40 = ofcolor(grid, x38)
    x41 = subgrid(x40, x39)
    return x41


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
