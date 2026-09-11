from collections import Counter


def copy(g):
    return [r[:] for r in g]


def bg(g):
    return Counter(v for row in g for v in row).most_common(1)[0][0]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    background = bg(g)
    out = copy(g)
    ps = [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == 1]
    for r, c in ps:
        for a in range(len(g)):
            out[a][c] = 1
        for b in range(len(g[0])):
            out[r][b] = 1
    for r, c in ps:
        out[r][c] = 2
        for dr in (-1, 1):
            for dc in (-1, 1):
                if 0 <= r + dr < len(g) and 0 <= c + dc < len(g[0]):
                    out[r + dr][c + dc] = 3
    return out
