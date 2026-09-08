"""Executable re-arc DSL program for ARC-AGI-2 task a48eeaf7.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.re_arc_dsl import (
    apply,
    argmax,
    argmin,
    backdrop,
    chain,
    color,
    compose,
    cover,
    equality,
    fgpartition,
    fill,
    fork,
    initset,
    lbind,
    manhattan,
    other,
    outbox,
    rbind,
    sfilter,
    size,
    toindices,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "a48eeaf7"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = fgpartition(grid)
    x1 = fork(equality, toindices, backdrop)
    x2 = sfilter(x0, x1)
    x3 = argmax(x2, size)
    x4 = other(x0, x3)
    x5 = color(x4)
    x6 = toindices(x4)
    x7 = outbox(x3)
    x8 = lbind(argmin, x7)
    x9 = lbind(lbind, manhattan)
    x10 = rbind(compose, initset)
    x11 = chain(x8, x10, x9)
    x12 = compose(x11, initset)
    x13 = apply(x12, x6)
    x14 = cover(grid, x4)
    x15 = fill(x14, x5, x13)
    return x15


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
