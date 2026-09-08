"""Executable re-arc DSL program for ARC-AGI-2 task fcb5c309.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    TWO,
    F,
    T,
    apply,
    argmax,
    argmin,
    backdrop,
    both,
    box,
    chain,
    colorcount,
    colorfilter,
    compose,
    contained,
    equality,
    extract,
    flip,
    fork,
    greater,
    lbind,
    minimum,
    objects,
    palette,
    rbind,
    remove,
    replace,
    shape,
    subgrid,
    toindices,
    toobject,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "fcb5c309"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, F)
    x1 = lbind(contained, F)
    x2 = compose(flip, x1)
    x3 = fork(equality, toindices, box)
    x4 = lbind(apply, x3)
    x5 = lbind(colorfilter, x0)
    x6 = chain(x2, x4, x5)
    x7 = rbind(greater, TWO)
    x8 = compose(minimum, shape)
    x9 = lbind(apply, x8)
    x10 = chain(x7, minimum, x9)
    x11 = lbind(colorfilter, x0)
    x12 = compose(x10, x11)
    x13 = fork(both, x6, x12)
    x14 = palette(grid)
    x15 = extract(x14, x13)
    x16 = palette(grid)
    x17 = remove(x15, x16)
    x18 = lbind(colorcount, grid)
    x19 = argmin(x17, x18)
    x20 = rbind(colorcount, x19)
    x21 = rbind(toobject, grid)
    x22 = chain(x20, x21, backdrop)
    x23 = colorfilter(x0, x15)
    x24 = argmax(x23, x22)
    x25 = subgrid(x24, grid)
    x26 = replace(x25, x15, x19)
    return x26


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
