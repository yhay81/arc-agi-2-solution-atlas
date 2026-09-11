from collections import Counter


def cp(g):
    return [row[:] for row in g]


def put(g, r, c, v):
    if 0 <= r < len(g) and 0 <= c < len(g[0]):
        g[r][c] = v


def points(g, color):
    return [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color]


def bg(g):
    return Counter(v for row in g for v in row).most_common(1)[0][0]


def solve(grid):
    g = grid
    h, w = (len(g), len(g[0]))
    out = cp(g)
    background = bg(g)
    for r, c in points(g, 5):
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            rr, cc = (r + dr, c + dc)
            if not (0 <= rr < h and 0 <= cc < w) or g[rr][cc] not in (0, 2):
                continue
            while 0 <= rr < h and 0 <= cc < w and (g[rr][cc] == 2):
                rr += dr
                cc += dc
            if not (0 <= rr < h and 0 <= cc < w) or g[rr][cc] != 0:
                continue
            tail = []
            tr, tc = (rr + dr, cc + dc)
            while 0 <= tr < h and 0 <= tc < w and (g[tr][tc] == 2):
                tail.append((tr, tc))
                tr += dr
                tc += dc
            nr, nc = (
                (0, 1 if cc < (w - 1) / 2 else -1) if dr else (1 if rr < (h - 1) / 2 else -1, 0)
            )
            for tr, tc in tail:
                out[tr][tc] = background
            for i in range(1, len(tail) + 1):
                put(out, rr + nr * i, cc + nc * i, 2)
    return out
