"""Executable re-arc DSL program for ARC-AGI-2 task 8efcae92.

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
    argmax,
    argmin,
    backdrop,
    chain,
    colorcount,
    compose,
    fork,
    height,
    intersection,
    lbind,
    merge,
    multiply,
    objects,
    outbox,
    palette,
    positive,
    rbind,
    remove,
    sfilter,
    size,
    subgrid,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "8efcae92"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, F)
    x1 = fork(multiply, height, width)
    x2 = argmax(x0, x1)
    x3 = remove(x2, x0)
    x4 = lbind(chain, positive)
    x5 = lbind(x4, size)
    x6 = rbind(compose, backdrop)
    x7 = lbind(lbind, intersection)
    x8 = chain(x5, x6, x7)
    x9 = chain(x8, backdrop, outbox)
    x10 = lbind(sfilter, x3)
    x11 = compose(x10, x9)
    x12 = chain(positive, size, x11)
    x13 = sfilter(x3, x12)
    x14 = compose(merge, x11)
    x15 = apply(x14, x13)
    x16 = rbind(subgrid, grid)
    x17 = apply(x16, x15)
    x18 = merge(x15)
    x19 = palette(x18)
    x20 = lbind(colorcount, x18)
    x21 = argmin(x19, x20)
    x22 = rbind(colorcount, x21)
    x23 = argmax(x17, x22)
    return x23


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
