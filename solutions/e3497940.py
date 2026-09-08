"""Executable re-arc DSL program for ARC-AGI-2 task e3497940.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    F,
    T,
    color,
    compose,
    first,
    flip,
    hsplit,
    lefthalf,
    matcher,
    merge,
    mostcolor,
    objects,
    paint,
    righthalf,
    sfilter,
    vmirror,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "e3497940"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = lefthalf(grid)
    x1 = righthalf(grid)
    x2 = vmirror(x1)
    x3 = width(grid)
    x4 = hsplit(grid, x3)
    x5 = first(x4)
    x6 = mostcolor(x5)
    x7 = objects(x2, T, F, F)
    x8 = matcher(color, x6)
    x9 = compose(flip, x8)
    x10 = sfilter(x7, x9)
    x11 = merge(x10)
    x12 = paint(x0, x11)
    return x12


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
