"""Executable re-arc DSL program for ARC-AGI-2 task 3f7978a0.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    DOWN,
    LEFT,
    RIGHT,
    TWO,
    UP,
    F,
    T,
    add,
    both,
    branch,
    chain,
    color,
    colorfilter,
    compose,
    double,
    either,
    equality,
    extract,
    first,
    fork,
    height,
    hline,
    initset,
    insert,
    lbind,
    lrcorner,
    objects,
    partition,
    rbind,
    sfilter,
    size,
    subgrid,
    ulcorner,
    vline,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "3f7978a0"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = partition(grid)
    x1 = objects(grid, T, F, F)
    x2 = compose(double, height)
    x3 = fork(equality, x2, size)
    x4 = compose(double, width)
    x5 = fork(equality, x4, size)
    x6 = fork(either, x3, x5)
    x7 = rbind(equality, TWO)
    x8 = lbind(colorfilter, x1)
    x9 = rbind(sfilter, vline)
    x10 = rbind(sfilter, hline)
    x11 = chain(x9, x8, color)
    x12 = chain(x7, size, x11)
    x13 = chain(x10, x8, color)
    x14 = chain(x7, size, x13)
    x15 = fork(either, x12, x14)
    x16 = fork(both, x6, x15)
    x17 = extract(x0, x16)
    x18 = color(x17)
    x19 = colorfilter(x1, x18)
    x20 = first(x19)
    x21 = vline(x20)
    x22 = ulcorner(x17)
    x23 = lrcorner(x17)
    x24 = branch(x21, UP, LEFT)
    x25 = add(x22, x24)
    x26 = branch(x21, DOWN, RIGHT)
    x27 = add(x23, x26)
    x28 = initset(x27)
    x29 = insert(x25, x28)
    x30 = subgrid(x29, grid)
    return x30


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
