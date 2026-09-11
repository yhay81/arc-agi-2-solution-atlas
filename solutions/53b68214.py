from collections import Counter


def bg(g):
    return Counter(v for r in g for v in r).most_common(1)[0][0]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    h, w = (len(g), len(g[0]))
    b = bg(g)
    p = {(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v != b}
    cands = []
    for dr in range(1, h):
        for dc in range(-w + 1, w):
            overlap = [((r, c), (r + dr, c + dc)) for r, c in p if 0 <= c + dc < w and r + dr < h]
            if overlap and all((g[a[0]][a[1]] == g[z[0]][z[1]] for a, z in overlap)):
                cands.append((len(overlap), -dr, -abs(dc), dr, dc))
    if not (cands):
        raise ValueError("task assumptions are not satisfied")
    _, _, _, dr, dc = max(cands)
    o = [row[:] for row in g] + [[b] * w for _ in range(max(0, 10 - h))]
    o = o[:10]
    for r in range(h, 10):
        for c in range(w):
            if 0 <= c - dc < w:
                o[r][c] = o[r - dr][c - dc]
    return o
