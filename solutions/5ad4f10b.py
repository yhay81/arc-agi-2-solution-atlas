"""Executable re-arc DSL program for ARC-AGI-2 task 5ad4f10b.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    ZERO,
    argmax,
    asindices,
    box,
    chain,
    compose,
    dneighbors,
    downscale,
    flip,
    fork,
    identity,
    intersection,
    interval,
    lbind,
    matcher,
    maximum,
    mostcolor,
    ofcolor,
    other,
    palette,
    positive,
    rbind,
    remove,
    replace,
    sfilter,
    shape,
    size,
    subgrid,
    switch,
    toobject,
    upscale,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "5ad4f10b"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = asindices(grid)
    x1 = box(x0)
    x2 = toobject(x1, grid)
    x3 = mostcolor(x2)
    x4 = palette(grid)
    x5 = remove(x3, x4)
    x6 = lbind(chain, size)
    x7 = rbind(x6, dneighbors)
    x8 = lbind(lbind, intersection)
    x9 = lbind(ofcolor, grid)
    x10 = chain(x7, x8, x9)
    x11 = rbind(matcher, ZERO)
    x12 = compose(x11, x10)
    x13 = chain(flip, positive, size)
    x14 = lbind(ofcolor, grid)
    x15 = fork(sfilter, x14, x12)
    x16 = compose(x13, x15)
    x17 = argmax(x5, x16)
    x18 = other(x5, x17)
    x19 = ofcolor(grid, x17)
    x20 = subgrid(x19, grid)
    x21 = switch(x20, x17, x18)
    x22 = replace(x21, x17, x3)
    x23 = lbind(downscale, x22)
    x24 = fork(upscale, x23, identity)
    x25 = matcher(x24, x22)
    x26 = shape(x22)
    x27 = maximum(x26)
    x28 = interval(ONE, x27, ONE)
    x29 = sfilter(x28, x25)
    x30 = maximum(x29)
    x31 = downscale(x22, x30)
    return x31


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
