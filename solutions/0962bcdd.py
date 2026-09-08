"""Executable re-arc DSL program for ARC-AGI-2 task 0962bcdd.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    F,
    T,
    combine,
    compose,
    connect,
    decrement,
    dneighbors,
    fork,
    hmirror,
    increment,
    lbind,
    leastcolor,
    lrcorner,
    mapply,
    mostcolor,
    objects,
    paint,
    recolor,
    toindices,
    ulcorner,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "0962bcdd"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, F, T, T)
    x1 = lbind(mapply, dneighbors)
    x2 = compose(x1, toindices)
    x3 = fork(recolor, mostcolor, x2)
    x4 = compose(decrement, ulcorner)
    x5 = compose(increment, lrcorner)
    x6 = fork(connect, x4, x5)
    x7 = compose(hmirror, x6)
    x8 = fork(combine, x6, x7)
    x9 = fork(recolor, leastcolor, x8)
    x10 = mapply(x3, x0)
    x11 = paint(grid, x10)
    x12 = mapply(x9, x0)
    x13 = paint(x11, x12)
    return x13


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
