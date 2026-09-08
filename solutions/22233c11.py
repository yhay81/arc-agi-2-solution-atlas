"""Executable re-arc DSL program for ARC-AGI-2 task 22233c11.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    EIGHT,
    TWO,
    T,
    chain,
    combine,
    compose,
    difference,
    fill,
    fork,
    halve,
    hfrontier,
    invert,
    lbind,
    mapply,
    objects,
    rbind,
    shape,
    shift,
    toindices,
    upscale,
    vfrontier,
    vmirror,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "22233c11"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, T, T)
    x1 = rbind(upscale, TWO)
    x2 = chain(invert, halve, shape)
    x3 = fork(combine, hfrontier, vfrontier)
    x4 = compose(x1, vmirror)
    x5 = fork(shift, x4, x2)
    x6 = compose(toindices, x5)
    x7 = lbind(mapply, x3)
    x8 = compose(x7, toindices)
    x9 = fork(difference, x6, x8)
    x10 = mapply(x9, x0)
    x11 = fill(grid, EIGHT, x10)
    return x11


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
