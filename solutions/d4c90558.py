def bounds(points):
    return (
        min(r for r, c in points),
        max(r for r, c in points),
        min(c for r, c in points),
        max(c for r, c in points),
    )


def solve(grid):
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
