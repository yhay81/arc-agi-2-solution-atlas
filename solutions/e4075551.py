"""Executable program for ARC-AGI-2 task e4075551.

Evidence:
- The program matches every provided training and test pair exactly.
- Provided test outputs were available during acceptance.

This entry was promoted from the private workbench and still requires an
independent editorial review of its general rule.
"""

TASK_ID = "e4075551"
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


def solve_e4075551(grid):
    red = [(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == 2]
    marks = [(r, c, v) for r, row in enumerate(grid) for c, v in enumerate(row) if v not in (0, 2)]
    if len(red) != 1 or len(marks) != 4:
        raise ValueError("Expected one red center and four colored side marks")
    upper, lower = min(marks, key=lambda x: x[0]), max(marks, key=lambda x: x[0])
    left, right = min(marks, key=lambda x: x[1]), max(marks, key=lambda x: x[1])
    if len({upper, lower, left, right}) != 4:
        raise ValueError("Side marks do not define four separate sides")
    top, bottom, lc, rc = upper[0], lower[0], left[1], right[1]
    pr, pc = red[0]
    if not (top < pr < bottom and lc < pc < rc):
        raise ValueError("Red point must be inside the indicated rectangle")
    out = [row[:] for row in grid]
    for r in range(top + 1, bottom):
        out[r][lc], out[r][rc], out[r][pc] = left[2], right[2], 5
    for c in range(lc, rc + 1):
        out[top][c], out[bottom][c] = upper[2], lower[2]
    for c in range(lc + 1, rc):
        out[pr][c] = 5
    out[pr][pc] = 2
    return out


solve = solve_e4075551
