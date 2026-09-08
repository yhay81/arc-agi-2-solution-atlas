"""Executable re-arc DSL program for ARC-AGI-2 task 54d82841.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    DOWN,
    FOUR,
    RIGHT,
    F,
    T,
    add,
    apply,
    astuple,
    branch,
    center,
    contained,
    decrement,
    delta,
    fill,
    first,
    height,
    last,
    lbind,
    mapply,
    objects,
    portrait,
    rbind,
    toindices,
    toivec,
    tojvec,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "54d82841"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, T)
    x1 = mapply(delta, x0)
    x2 = first(x0)
    x3 = toindices(x2)
    x4 = rbind(contained, x3)
    x5 = portrait(x2)
    x6 = apply(first, x1)
    x7 = apply(last, x1)
    x8 = branch(x5, x6, x7)
    x9 = branch(x5, RIGHT, DOWN)
    x10 = delta(x2)
    x11 = center(x10)
    x12 = add(x11, x9)
    x13 = x4(x12)
    x14 = branch(x5, width, height)
    x15 = branch(x5, rbind, lbind)
    x16 = x14(grid)
    x17 = decrement(x16)
    x18 = x15(astuple, x17)
    x19 = branch(x5, toivec, tojvec)
    x20 = branch(x13, x19, x18)
    x21 = apply(x20, x8)
    x22 = fill(grid, FOUR, x21)
    return x22


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
