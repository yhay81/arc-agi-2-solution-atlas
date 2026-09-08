"""Executable program for ARC-AGI-2 task c8b7cc0f.

Evidence:
- The program matches every provided training and test pair exactly.
- Provided test outputs were available during acceptance.

This entry was promoted from the private workbench and still requires an
independent editorial review of its general rule.
"""

TASK_ID = "c8b7cc0f"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("verified-program",)


def solve_c8b7cc0f(grid):
    blue = [(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == 1]
    if not blue:
        raise ValueError("Missing blue frame")
    top, bottom = min(r for r, c in blue), max(r for r, c in blue)
    left, right = min(c for r, c in blue), max(c for r, c in blue)
    points = [
        grid[r][c]
        for r in range(top + 1, bottom)
        for c in range(left + 1, right)
        if grid[r][c] not in (0, 1)
    ]
    if len(set(points)) != 1 or len(points) > 9:
        raise ValueError("Expected one interior point color and one to nine points")
    color = points[0]
    return [[color if 3 * r + c < len(points) else 0 for c in range(3)] for r in range(3)]


solve = solve_c8b7cc0f
