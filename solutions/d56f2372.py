"""Executable program for ARC-AGI-2 task d56f2372.

Evidence:
- The program matches every provided training and test pair exactly.
- Provided test outputs were available during acceptance.

This entry was promoted from the private workbench and still requires an
independent editorial review of its general rule.
"""

TASK_ID = "d56f2372"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("verified-program",)


def solve(grid):
    colors = sorted({v for row in grid for v in row} - {0})
    candidates = []
    for color in colors:
        points = [(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == color]
        top = min(r for r, c in points)
        bottom = max(r for r, c in points)
        left = min(c for r, c in points)
        right = max(c for r, c in points)
        patch = [
            [v if v == color else 0 for v in row[left : right + 1]]
            for row in grid[top : bottom + 1]
        ]
        if all(row == row[::-1] for row in patch):
            candidates.append(patch)
    if len(candidates) != 1:
        raise ValueError("Expected one left-right symmetric color object")
    return candidates[0]
