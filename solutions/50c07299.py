"""Executable program for ARC-AGI-2 task 50c07299.

Evidence:
- The program matches every provided training and test pair exactly.
- Provided test outputs were available during acceptance.

This entry was promoted from the private workbench and still requires an
independent editorial review of its general rule.
"""

TASK_ID = "50c07299"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("verified-program",)


def solve(grid):
    from collections import Counter

    background = Counter(value for row in grid for value in row).most_common(1)[0][0]
    points = [
        (r, c, value)
        for r, row in enumerate(grid)
        for c, value in enumerate(row)
        if value != background
    ]
    r, c, color = min(points)
    output = [[background] * len(grid[0]) for _ in grid]
    for k in range(1, len(points) + 2):
        if 0 <= r - k < len(grid) and 0 <= c + k < len(grid[0]):
            output[r - k][c + k] = color
    return output
