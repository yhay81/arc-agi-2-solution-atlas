"""Executable re-arc DSL program for ARC-AGI-2 task fcc82909.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    DOWN,
    RIGHT,
    THREE,
    F,
    T,
    add,
    backdrop,
    chain,
    compose,
    decrement,
    fill,
    fork,
    initset,
    insert,
    lbind,
    llcorner,
    mapply,
    numcolors,
    objects,
    rbind,
    toivec,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "fcc82909"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, F, F, T)
    x1 = lbind(add, DOWN)
    x2 = compose(x1, llcorner)
    x3 = rbind(add, RIGHT)
    x4 = compose(x3, x2)
    x5 = chain(toivec, decrement, numcolors)
    x6 = fork(add, x4, x5)
    x7 = compose(initset, x6)
    x8 = fork(insert, x2, x7)
    x9 = compose(backdrop, x8)
    x10 = mapply(x9, x0)
    x11 = fill(grid, THREE, x10)
    return x11


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
