"""Executable program for ARC-AGI-2 task c3202e5a.

Evidence:
- The program matches every provided training and test pair exactly.
- Provided test outputs were available during acceptance.

This entry was promoted from the private workbench and still requires an
independent editorial review of its general rule.
"""

from itertools import pairwise

TASK_ID = "c3202e5a"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("verified-program",)


def components(points):
    remaining, result = set(points), []
    while remaining:
        start = min(remaining)
        remaining.remove(start)
        group, stack = {start}, [start]
        while stack:
            r, c = stack.pop()
            for neighbor in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if neighbor in remaining:
                    remaining.remove(neighbor)
                    group.add(neighbor)
                    stack.append(neighbor)
        result.append(group)
    return result


def bounds(points):
    return (
        min(r for r, c in points),
        max(r for r, c in points),
        min(c for r, c in points),
        max(c for r, c in points),
    )


def solve_c3202e5a(grid):
    height, width = len(grid), len(grid[0])
    rows = [r for r, row in enumerate(grid) if len(set(row)) == 1 and row[0] != 0]
    cols = [c for c in range(width) if len({row[c] for row in grid}) == 1 and grid[0][c] != 0]
    if not rows or not cols:
        raise ValueError("Missing full grid separator rows or columns")
    boundaries_r, boundaries_c = [-1, *rows, height], [-1, *cols, width]
    candidates = []
    for a, b in pairwise(boundaries_r):
        for c, d in pairwise(boundaries_c):
            if b <= a + 1 or d <= c + 1:
                continue
            patch = [row[c + 1 : d] for row in grid[a + 1 : b]]
            if len({v for row in patch for v in row} - {0}) == 1:
                candidates.append(patch)
    if len(candidates) != 1:
        raise ValueError("Expected one monochromatic nonempty panel")
    return candidates[0]


solve = solve_c3202e5a
