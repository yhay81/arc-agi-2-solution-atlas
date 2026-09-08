"""Executable re-arc DSL program for ARC-AGI-2 task 1e32b0e9.

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
    argmin,
    box,
    canvas,
    color,
    colorcount,
    compose,
    contained,
    difference,
    fill,
    first,
    frontiers,
    hconcat,
    last,
    lbind,
    leastcommon,
    mapply,
    matcher,
    merge,
    normalize,
    objects,
    ofcolor,
    other,
    palette,
    rbind,
    remove,
    sfilter,
    shape,
    shift,
    toindices,
    totuple,
    ulcorner,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "1e32b0e9"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = frontiers(grid)
    x1 = totuple(x0)
    x2 = apply(color, x1)
    x3 = leastcommon(x2)
    x4 = matcher(color, x3)
    x5 = sfilter(x0, x4)
    x6 = merge(x5)
    x7 = color(x6)
    x8 = shape(grid)
    x9 = canvas(x7, x8)
    x10 = hconcat(grid, x9)
    x11 = objects(x10, F, T, T)
    x12 = first(x11)
    x13 = box(x12)
    x14 = rbind(contained, x13)
    x15 = compose(x14, last)
    x16 = sfilter(x12, x15)
    x17 = color(x16)
    x18 = palette(grid)
    x19 = remove(x7, x18)
    x20 = other(x19, x17)
    x21 = rbind(colorcount, x17)
    x22 = argmin(x11, x21)
    x23 = apply(ulcorner, x11)
    x24 = normalize(x22)
    x25 = matcher(first, x20)
    x26 = sfilter(x24, x25)
    x27 = toindices(x26)
    x28 = lbind(shift, x27)
    x29 = mapply(x28, x23)
    x30 = ofcolor(grid, x20)
    x31 = difference(x29, x30)
    x32 = fill(grid, x7, x31)
    return x32


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
