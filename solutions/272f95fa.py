"""Executable re-arc DSL program for ARC-AGI-2 task 272f95fa.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    FOUR,
    ONE,
    ORIGIN,
    SIX,
    THREE,
    TWO,
    F,
    T,
    apply,
    argmax,
    argmin,
    bordering,
    colorfilter,
    compose,
    extract,
    fill,
    flip,
    hmatching,
    index,
    lbind,
    leftmost,
    objects,
    rbind,
    remove,
    sfilter,
    toindices,
    uppermost,
    vmatching,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "272f95fa"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, F)
    x1 = index(grid, ORIGIN)
    x2 = colorfilter(x0, x1)
    x3 = apply(toindices, x2)
    x4 = rbind(bordering, grid)
    x5 = compose(flip, x4)
    x6 = extract(x3, x5)
    x7 = remove(x6, x3)
    x8 = lbind(vmatching, x6)
    x9 = lbind(hmatching, x6)
    x10 = sfilter(x7, x8)
    x11 = sfilter(x7, x9)
    x12 = argmin(x10, uppermost)
    x13 = argmax(x10, uppermost)
    x14 = argmin(x11, leftmost)
    x15 = argmax(x11, leftmost)
    x16 = fill(grid, SIX, x6)
    x17 = fill(x16, TWO, x12)
    x18 = fill(x17, ONE, x13)
    x19 = fill(x18, FOUR, x14)
    x20 = fill(x19, THREE, x15)
    return x20


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
