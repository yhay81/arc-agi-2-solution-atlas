"""Scale the grid by the number of distinct colors.

Rule:
1. Count the distinct colors in the input and call that number ``k``.
2. Replace every input cell with a ``k`` by ``k`` block of the same color.

Evidence:
- The implementation matches all seven provided training pairs.
- The implementation matches the provided test pair.
- The test output was used when accepting this program.

Known ambiguity:
- The examples contain no black cells, so they do not establish whether color 0
  should contribute to the color count.
"""

from arc_agi_2_atlas.types import Grid

TASK_ID = "d4b1c2b1"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("color-counting", "scaling", "nearest-neighbor-expansion")


def solve(grid: Grid) -> Grid:
    """Replace each cell with a k by k block, where k is the color count."""
    factor = len({cell for row in grid for cell in row})
    return [[cell for cell in row for _ in range(factor)] for row in grid for _ in range(factor)]
