"""Executable re-arc DSL program for ARC-AGI-2 task c8cbb738.

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
    asindices,
    astuple,
    box,
    canvas,
    center,
    chain,
    compose,
    double,
    fgpartition,
    fork,
    height,
    identity,
    initset,
    intersection,
    lbind,
    manhattan,
    mapply,
    maximum,
    mostcolor,
    multiply,
    normalize,
    paint,
    shift,
    size,
    subtract,
    toindices,
    valmax,
    width,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "c8cbb738"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = fgpartition(grid)
    x1 = valmax(x0, height)
    x2 = valmax(x0, width)
    x3 = astuple(x1, x2)
    x4 = mostcolor(grid)
    x5 = canvas(x4, x3)
    x6 = asindices(x5)
    x7 = apply(normalize, x0)
    x8 = box(x6)
    x9 = maximum(x3)
    x10 = double(x9)
    x11 = asindices(x5)
    x12 = center(x11)
    x13 = initset(x12)
    x14 = lbind(manhattan, x13)
    x15 = lbind(multiply, x10)
    x16 = lbind(intersection, x8)
    x17 = chain(x15, size, x16)
    x18 = lbind(fork, subtract)
    x19 = lbind(chain, x17)
    x20 = lbind(x19, toindices)
    x21 = lbind(lbind, shift)
    x22 = compose(x20, x21)
    x23 = lbind(chain, x14)
    x24 = compose(initset, center)
    x25 = lbind(x23, x24)
    x26 = lbind(lbind, shift)
    x27 = compose(x25, x26)
    x28 = lbind(argmax, x6)
    x29 = fork(x18, x22, x27)
    x30 = compose(x28, x29)
    x31 = fork(shift, identity, x30)
    x32 = mapply(x31, x7)
    x33 = paint(x5, x32)
    return x33


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
