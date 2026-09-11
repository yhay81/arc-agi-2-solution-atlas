from collections import Counter


def solve(grid):
    vals = Counter(v for row in grid for v in row if v)
    markers = [v for v, n in vals.items() if n == 4]
    if len(markers) != 1:
        return [r[:] for r in grid]
    objects = [v for v in vals if v != markers[0]]
    if len(objects) != 1:
        return [r[:] for r in grid]
    pts = [(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == markers[0]]
    top, bottom = min(r for r, _ in pts) + 1, max(r for r, _ in pts) - 1
    left, right = min(c for _, c in pts) + 1, max(c for _, c in pts) - 1
    if top >= bottom or left >= right:
        return [r[:] for r in grid]
    boundary = [
        (r, c)
        for r in range(top, bottom + 1)
        for c in range(left, right + 1)
        if r in (top, bottom) or c in (left, right)
    ]
    if any(grid[r][c] not in (0, objects[0]) for r, c in boundary):
        return [r[:] for r in grid]
    out = [r[:] for r in grid]
    for r, c in boundary:
        out[r][c] = objects[0]
    return out
