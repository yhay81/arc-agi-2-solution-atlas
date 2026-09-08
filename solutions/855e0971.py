"""Executable re-arc DSL program for ARC-AGI-2 task 855e0971.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    THREE,
    F,
    T,
    apply,
    argmax,
    branch,
    chain,
    colorfilter,
    compose,
    contained,
    dedupe,
    difference,
    dmirror,
    flip,
    fork,
    greater,
    identity,
    lbind,
    mapply,
    neighbors,
    objects,
    ofcolor,
    order,
    paint,
    palette,
    rbind,
    recolor,
    sfilter,
    size,
    subgrid,
    toobject,
    uppermost,
    vfrontier,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "855e0971"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = lbind(greater, THREE)
    x1 = chain(x0, size, dedupe)
    x2 = apply(x1, grid)
    x3 = contained(F, x2)
    x4 = flip(x3)
    x5 = branch(x4, identity, dmirror)
    x6 = x5(grid)
    x7 = rbind(toobject, grid)
    x8 = chain(palette, x7, neighbors)
    x9 = lbind(chain, flip)
    x10 = rbind(x9, x8)
    x11 = lbind(lbind, contained)
    x12 = compose(x10, x11)
    x13 = lbind(ofcolor, grid)
    x14 = fork(sfilter, x13, x12)
    x15 = compose(size, x14)
    x16 = palette(grid)
    x17 = argmax(x16, x15)
    x18 = objects(x6, T, T, F)
    x19 = colorfilter(x18, x17)
    x20 = difference(x18, x19)
    x21 = rbind(subgrid, x6)
    x22 = order(x20, uppermost)
    x23 = apply(x21, x22)
    x24 = lbind(recolor, x17)
    x25 = lbind(mapply, vfrontier)
    x26 = rbind(ofcolor, x17)
    x27 = chain(x24, x25, x26)
    x28 = fork(paint, identity, x27)
    x29 = mapply(x28, x23)
    x30 = x5(x29)
    return x30


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
