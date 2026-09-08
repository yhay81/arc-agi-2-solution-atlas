"""Executable re-arc DSL program for ARC-AGI-2 task 508bd3b6.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    DOWN_LEFT,
    NEG_UNITY,
    ONE,
    THREE,
    UNITY,
    UP_RIGHT,
    F,
    T,
    apply,
    argmin,
    asindices,
    backdrop,
    branch,
    chain,
    colorfilter,
    combine,
    compose,
    contained,
    difference,
    equality,
    extract,
    fill,
    fork,
    greater,
    height,
    initset,
    intersection,
    lbind,
    leftmost,
    manhattan,
    matcher,
    maximum,
    objects,
    ofcolor,
    outbox,
    palette,
    rbind,
    shape,
    shoot,
    ulcorner,
    uppermost,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "508bd3b6"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, F)
    x1 = palette(grid)
    x2 = compose(maximum, shape)
    x3 = lbind(apply, x2)
    x4 = lbind(colorfilter, x0)
    x5 = chain(maximum, x3, x4)
    x6 = matcher(x5, ONE)
    x7 = extract(x1, x6)
    x8 = lbind(ofcolor, grid)
    x9 = compose(backdrop, x8)
    x10 = fork(equality, x8, x9)
    x11 = extract(x1, x10)
    x12 = ofcolor(grid, x11)
    x13 = ofcolor(grid, x7)
    x14 = rbind(manhattan, x12)
    x15 = compose(x14, initset)
    x16 = argmin(x13, x15)
    x17 = ulcorner(x13)
    x18 = contained(x17, x13)
    x19 = shoot(x16, UNITY)
    x20 = shoot(x16, NEG_UNITY)
    x21 = combine(x19, x20)
    x22 = shoot(x16, UP_RIGHT)
    x23 = shoot(x16, DOWN_LEFT)
    x24 = combine(x22, x23)
    x25 = branch(x18, x21, x24)
    x26 = asindices(grid)
    x27 = outbox(x12)
    x28 = intersection(x26, x27)
    x29 = intersection(x28, x25)
    x30 = initset(x16)
    x31 = rbind(manhattan, x30)
    x32 = compose(x31, initset)
    x33 = argmin(x29, x32)
    x34 = height(x12)
    x35 = height(grid)
    x36 = equality(x34, x35)
    x37 = leftmost(x13)
    x38 = leftmost(x12)
    x39 = greater(x37, x38)
    x40 = uppermost(x13)
    x41 = uppermost(x12)
    x42 = greater(x40, x41)
    x43 = lbind(shoot, x33)
    x44 = branch(x39, UNITY, NEG_UNITY)
    x45 = branch(x39, UP_RIGHT, DOWN_LEFT)
    x46 = branch(x42, UNITY, NEG_UNITY)
    x47 = branch(x42, DOWN_LEFT, UP_RIGHT)
    x48 = branch(x36, x44, x46)
    x49 = branch(x36, x45, x47)
    x50 = x43(x48)
    x51 = x43(x49)
    x52 = combine(x50, x51)
    x53 = difference(x52, x13)
    x54 = fill(grid, THREE, x53)
    return x54


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
