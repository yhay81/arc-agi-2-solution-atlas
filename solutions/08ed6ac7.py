"""Executable re-arc DSL program for ARC-AGI-2 task 08ed6ac7.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    apply,
    astuple,
    chain,
    combine,
    compose,
    dedupe,
    dmirror,
    extract,
    first,
    fork,
    height,
    identity,
    increment,
    interval,
    last,
    lbind,
    matcher,
    mostcommon,
    order,
    pair,
    rbind,
    repeat,
    sfilter,
    size,
    subtract,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "08ed6ac7"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = first(grid)
    x1 = mostcommon(x0)
    x2 = dmirror(grid)
    x3 = matcher(identity, x1)
    x4 = rbind(sfilter, x3)
    x5 = compose(size, x4)
    x6 = apply(x5, x2)
    x7 = dedupe(x6)
    x8 = order(x7, identity)
    x9 = size(x8)
    x10 = increment(x9)
    x11 = increment(x10)
    x12 = interval(ONE, x11, ONE)
    x13 = pair(x8, x12)
    x14 = height(grid)
    x15 = astuple(x14, x1)
    x16 = repeat(x15, ONE)
    x17 = combine(x16, x13)
    x18 = lbind(extract, x17)
    x19 = lbind(matcher, first)
    x20 = chain(last, x18, x19)
    x21 = compose(x20, x5)
    x22 = fork(subtract, height, x5)
    x23 = fork(repeat, x21, x22)
    x24 = lbind(repeat, x1)
    x25 = compose(x24, x5)
    x26 = fork(combine, x25, x23)
    x27 = apply(x26, x2)
    x28 = dmirror(x27)
    return x28


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
