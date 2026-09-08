"""Executable re-arc DSL program for ARC-AGI-2 task b775ac94.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ORIGIN,
    ZERO,
    F,
    T,
    backdrop,
    branch,
    chain,
    compose,
    contained,
    difference,
    extract,
    first,
    fork,
    hmirror,
    identity,
    initset,
    last,
    lbind,
    mapply,
    matcher,
    mostcolor,
    multiply,
    neighbors,
    objects,
    paint,
    rapply,
    rbind,
    recolor,
    sfilter,
    shape,
    shift,
    vmirror,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "b775ac94"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, F, T, T)
    x1 = neighbors(ORIGIN)
    x2 = lbind(extract, x1)
    x3 = matcher(first, ZERO)
    x4 = matcher(last, ZERO)
    x5 = rbind(branch, hmirror)
    x6 = rbind(x5, identity)
    x7 = rbind(branch, vmirror)
    x8 = rbind(x7, identity)
    x9 = compose(x6, x3)
    x10 = compose(x8, x4)
    x11 = fork(compose, x9, x10)
    x12 = lbind(matcher, first)
    x13 = compose(x12, mostcolor)
    x14 = fork(sfilter, identity, x13)
    x15 = fork(difference, identity, x14)
    x16 = lbind(rbind, multiply)
    x17 = chain(x16, shape, x14)
    x18 = lbind(lbind, shift)
    x19 = chain(x18, backdrop, x14)
    x20 = fork(compose, x19, x17)
    x21 = lbind(lbind, contained)
    x22 = compose(x21, last)
    x23 = rbind(compose, x22)
    x24 = lbind(rbind, compose)
    x25 = chain(x23, x24, x20)
    x26 = lbind(fork, recolor)
    x27 = lbind(x26, first)
    x28 = lbind(fork, shift)
    x29 = lbind(chain, x11)
    x30 = lbind(x29, x2)
    x31 = rbind(compose, x2)
    x32 = compose(x31, x17)
    x33 = fork(compose, x32, x25)
    x34 = compose(x30, x25)
    x35 = lbind(chain, first)
    x36 = lbind(rbind, rapply)
    x37 = compose(x36, x14)
    x38 = lbind(compose, initset)
    x39 = compose(x38, x34)
    x40 = fork(x35, x37, x39)
    x41 = compose(x27, x40)
    x42 = fork(x28, x41, x33)
    x43 = fork(mapply, x42, x15)
    x44 = mapply(x43, x0)
    x45 = paint(grid, x44)
    return x45


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
