"""Executable re-arc DSL program for ARC-AGI-2 task ce602527.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    TWO,
    asobject,
    bordering,
    branch,
    canvas,
    color,
    downscale,
    extract,
    fgpartition,
    first,
    last,
    mostcolor,
    normalize,
    occurrences,
    paint,
    positive,
    rbind,
    remove,
    replace,
    shape,
    size,
    totuple,
    upscale,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "ce602527"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = fgpartition(grid)
    x1 = rbind(bordering, grid)
    x2 = extract(x0, x1)
    x3 = remove(x2, x0)
    x4 = totuple(x3)
    x5 = first(x4)
    x6 = last(x4)
    x7 = color(x5)
    x8 = mostcolor(grid)
    x9 = shape(x5)
    x10 = canvas(x8, x9)
    x11 = normalize(x5)
    x12 = paint(x10, x11)
    x13 = upscale(x12, TWO)
    x14 = shape(x6)
    x15 = canvas(x8, x14)
    x16 = normalize(x6)
    x17 = paint(x15, x16)
    x18 = upscale(x17, TWO)
    x19 = shape(x2)
    x20 = canvas(x8, x19)
    x21 = normalize(x2)
    x22 = paint(x20, x21)
    x23 = color(x2)
    x24 = replace(x22, x23, x7)
    x25 = asobject(x24)
    x26 = occurrences(x13, x25)
    x27 = size(x26)
    x28 = positive(x27)
    x29 = downscale(x13, TWO)
    x30 = downscale(x18, TWO)
    x31 = branch(x28, x29, x30)
    return x31


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
