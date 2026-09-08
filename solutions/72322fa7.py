"""Executable re-arc DSL program for ARC-AGI-2 task 72322fa7.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    TWO,
    F,
    T,
    apply,
    chain,
    combine,
    compose,
    first,
    fork,
    identity,
    invert,
    last,
    lbind,
    mapply,
    matcher,
    normalize,
    numcolors,
    objects,
    occurrences,
    paint,
    palette,
    sfilter,
    shift,
    totuple,
    ulcorner,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "72322fa7"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, F, T, T)
    x1 = matcher(numcolors, TWO)
    x2 = sfilter(x0, x1)
    x3 = apply(normalize, x2)
    x4 = chain(first, totuple, palette)
    x5 = chain(last, totuple, palette)
    x6 = lbind(matcher, first)
    x7 = compose(x6, x4)
    x8 = lbind(matcher, first)
    x9 = compose(x8, x5)
    x10 = fork(sfilter, identity, x7)
    x11 = fork(sfilter, identity, x9)
    x12 = lbind(occurrences, grid)
    x13 = chain(invert, ulcorner, x10)
    x14 = chain(invert, ulcorner, x11)
    x15 = lbind(lbind, shift)
    x16 = fork(shift, identity, x13)
    x17 = fork(shift, identity, x14)
    x18 = compose(x15, x16)
    x19 = compose(x12, x10)
    x20 = fork(mapply, x18, x19)
    x21 = compose(x15, x17)
    x22 = compose(x12, x11)
    x23 = fork(mapply, x21, x22)
    x24 = fork(combine, x20, x23)
    x25 = mapply(x24, x3)
    x26 = paint(grid, x25)
    return x26


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
