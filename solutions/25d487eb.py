"""Executable re-arc DSL program for ARC-AGI-2 task 25d487eb.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    F,
    T,
    apply,
    compose,
    difference,
    dneighbors,
    extract,
    first,
    fork,
    identity,
    last,
    lbind,
    leastcolor,
    mapply,
    matcher,
    mostcolor,
    objects,
    recolor,
    sfilter,
    shoot,
    subtract,
    underpaint,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "25d487eb"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, F, F, T)
    x1 = lbind(matcher, first)
    x2 = compose(x1, leastcolor)
    x3 = lbind(matcher, first)
    x4 = compose(x3, mostcolor)
    x5 = fork(extract, identity, x2)
    x6 = compose(last, x5)
    x7 = compose(dneighbors, x6)
    x8 = lbind(apply, last)
    x9 = fork(sfilter, identity, x4)
    x10 = compose(x8, x9)
    x11 = fork(difference, x7, x10)
    x12 = compose(first, x11)
    x13 = fork(subtract, x6, x12)
    x14 = fork(shoot, x6, x13)
    x15 = fork(recolor, leastcolor, x14)
    x16 = mapply(x15, x0)
    x17 = underpaint(grid, x16)
    return x17


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
