from collections import Counter


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    h, w = (len(g), len(g[0]))
    r = next((r for r, row in enumerate(g) if len(set(row)) == 1))
    c = next(c for c in range(w) if len({g[r][c] for r in range(h)}) == 1)
    color = g[r][c]
    out = [[color] * 3 for _ in range(3)]
    for rr, (a, b) in enumerate(((0, r), (r + 1, h))):
        for cc, (left, right) in enumerate(((0, c), (c + 1, w))):
            out[rr * 2][cc * 2] = Counter(
                g[x][y] for x in range(a, b) for y in range(left, right)
            ).most_common(1)[0][0]
    return out
