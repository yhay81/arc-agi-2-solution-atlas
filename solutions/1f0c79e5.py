"""Executable re-arc DSL program for ARC-AGI-2 task 1f0c79e5.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    NEG_ONE,
    TWO,
    F,
    T,
    add,
    apply,
    chain,
    compose,
    double,
    first,
    fork,
    lbind,
    mapply,
    matcher,
    normalize,
    objects,
    other,
    paint,
    palette,
    rbind,
    recolor,
    sfilter,
    shoot,
    toindices,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "1f0c79e5"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, F, F, T)
    x1 = rbind(other, TWO)
    x2 = compose(x1, palette)
    x3 = matcher(first, TWO)
    x4 = rbind(sfilter, x3)
    x5 = compose(x4, normalize)
    x6 = lbind(apply, double)
    x7 = chain(x6, toindices, x5)
    x8 = rbind(add, NEG_ONE)
    x9 = lbind(apply, x8)
    x10 = compose(x9, x7)
    x11 = lbind(rbind, shoot)
    x12 = rbind(compose, x11)
    x13 = lbind(rbind, mapply)
    x14 = chain(x12, x13, toindices)
    x15 = fork(mapply, x14, x10)
    x16 = fork(recolor, x2, x15)
    x17 = mapply(x16, x0)
    x18 = paint(grid, x17)
    return x18


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
