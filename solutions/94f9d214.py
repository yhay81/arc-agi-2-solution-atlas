"""Executable re-arc DSL program for ARC-AGI-2 task 94f9d214.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    TWO,
    TWO_BY_TWO,
    apply,
    astuple,
    canvas,
    chain,
    compose,
    extract,
    fill,
    first,
    hsplit,
    initset,
    intersection,
    last,
    lbind,
    matcher,
    numcolors,
    ofcolor,
    palette,
    rapply,
    rbind,
    shape,
    vsplit,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "94f9d214"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = astuple(vsplit, hsplit)
    x1 = rbind(rbind, TWO)
    x2 = rbind(rapply, grid)
    x3 = initset(x1)
    x4 = lbind(rapply, x3)
    x5 = chain(first, x2, x4)
    x6 = lbind(apply, numcolors)
    x7 = compose(x6, x5)
    x8 = matcher(x7, TWO_BY_TWO)
    x9 = extract(x0, x8)
    x10 = x9(grid, TWO)
    x11 = first(x10)
    x12 = last(x10)
    x13 = palette(x11)
    x14 = palette(x12)
    x15 = intersection(x13, x14)
    x16 = first(x15)
    x17 = shape(x11)
    x18 = canvas(x16, x17)
    x19 = ofcolor(x11, x16)
    x20 = ofcolor(x12, x16)
    x21 = intersection(x19, x20)
    x22 = fill(x18, TWO, x21)
    return x22


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
