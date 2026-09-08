"""Executable program for ARC-AGI-2 task d4c90558.

Evidence:
- The program matches every provided training and test pair exactly.
- Provided test outputs were available during acceptance.

This entry was promoted from the private workbench and still requires an
independent editorial review of its general rule.
"""

TASK_ID = "d4c90558"
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


def solve_d4c90558(grid):
    colors = sorted({v for row in grid for v in row} - {0, 5})
    entries = []
    for color in colors:
        frame = [(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == color]
        top, bottom, left, right = bounds(frame)
        count = sum(grid[r][c] == 5 for r in range(top + 1, bottom) for c in range(left + 1, right))
        entries.append((count, color))
    if not entries or len({count for count, color in entries}) != len(entries):
        raise ValueError("Expected distinct gray counts for every colored frame")
    entries.sort()
    width = entries[-1][0]
    return [[color] * count + [0] * (width - count) for count, color in entries]


solve = solve_d4c90558
