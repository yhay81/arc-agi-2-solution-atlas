"""Executable program for ARC-AGI-2 task bf89d739.

Evidence:
- The program matches every provided training and test pair exactly.
- Provided test outputs were available during acceptance.

This entry was promoted from the private workbench and still requires an
independent editorial review of its general rule.
"""

TASK_ID = "bf89d739"
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


def solve_bf89d739(grid):
    red = [(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == 2]
    pairs = [
        (a, b) for i, a in enumerate(red) for b in red[i + 1 :] if a[0] == b[0] or a[1] == b[1]
    ]
    if len(pairs) != 1:
        raise ValueError("Expected one aligned pair defining the trunk")
    a, b = pairs[0]
    out = [row[:] for row in grid]
    if a[0] == b[0]:
        for c in range(min(a[1], b[1]), max(a[1], b[1]) + 1):
            out[a[0]][c] = 3
        for r, c in red:
            if not min(a[1], b[1]) <= c <= max(a[1], b[1]):
                raise ValueError("Point projects outside the trunk")
            for rr in range(min(r, a[0]), max(r, a[0]) + 1):
                out[rr][c] = 3
    else:
        for r in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
            out[r][a[1]] = 3
        for r, c in red:
            if not min(a[0], b[0]) <= r <= max(a[0], b[0]):
                raise ValueError("Point projects outside the trunk")
            for cc in range(min(c, a[1]), max(c, a[1]) + 1):
                out[r][cc] = 3
    for r, c in red:
        out[r][c] = 2
    return out


solve = solve_bf89d739
