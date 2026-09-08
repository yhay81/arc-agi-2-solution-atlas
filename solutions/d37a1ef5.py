"""Executable program for ARC-AGI-2 task d37a1ef5.

Evidence:
- The program matches every provided training and test pair exactly.
- Provided test outputs were available during acceptance.

This entry was promoted from the private workbench and still requires an
independent editorial review of its general rule.
"""

TASK_ID = "d37a1ef5"
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


def solve_d37a1ef5(grid):
    frame = {(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == 2}
    gray = {(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == 5}
    if not frame or not gray:
        raise ValueError("Expected red frame and gray pattern")
    top, bottom, left, right = bounds(frame)
    a, b, c, d = bounds(gray)
    out = [row[:] for row in grid]
    for r in range(top + 1, bottom):
        for col in range(left + 1, right):
            if not (a <= r <= b and c <= col <= d):
                out[r][col] = 2
    return out


solve = solve_d37a1ef5
