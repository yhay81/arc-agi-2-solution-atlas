from collections import Counter


def mode(values):
    return Counter(values).most_common(1)[0][0]


def bounds(points):
    rs, cs = zip(*points)
    return min(rs), min(cs), max(rs), max(cs)


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    bg = mode([v for row in a for v in row])
    color = next(c for c in {v for row in a for v in row} if c != bg)
    n = 3 * (len(a) - 1) + 1
    out = [[bg] * n for _ in range(n)]
    r, c, b, d = bounds(
        [(y, x) for y, row in enumerate(a) for x, v in enumerate(row) if v == color]
    )
    length = 2 * (b - r + 1)
    right = c > 0
    bottom = r > 0
    for y in range(length):
        for x in range(length):
            if y == length - 1 or x == length - 1 or y + x == length - 1:
                out[n - length + y if bottom else length - 1 - y][
                    n - length + x if right else length - 1 - x
                ] = color
    return out
