"""Executable re-arc DSL program for ARC-AGI-2 task c9f8e694.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    ORIGIN,
    ZERO,
    argmax,
    astuple,
    chain,
    cmirror,
    combine,
    compose,
    crop,
    dedupe,
    dmirror,
    fill,
    first,
    height,
    hupscale,
    identity,
    initset,
    ofcolor,
    rapply,
    rbind,
    size,
    vmirror,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "c9f8e694"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = astuple(identity, dmirror)
    x1 = astuple(cmirror, vmirror)
    x2 = combine(x0, x1)
    x3 = compose(first, dmirror)
    x4 = chain(size, dedupe, x3)
    x5 = rbind(rapply, grid)
    x6 = compose(first, x5)
    x7 = chain(x4, x6, initset)
    x8 = argmax(x2, x7)
    x9 = x8(grid)
    x10 = height(x9)
    x11 = width(x9)
    x12 = ofcolor(x9, ZERO)
    x13 = astuple(x10, ONE)
    x14 = crop(x9, ORIGIN, x13)
    x15 = hupscale(x14, x11)
    x16 = fill(x15, ZERO, x12)
    x17 = x8(x16)
    return x17


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
