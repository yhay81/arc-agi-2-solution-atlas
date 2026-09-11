from collections import Counter


def pts(g, color):
    return {(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color}


def box(p):
    return (
        min((r for r, c in p)),
        max((r for r, c in p)),
        min((c for r, c in p)),
        max((c for r, c in p)),
    )


def paint(g, p, color):
    for r, c in p:
        if 0 <= r < len(g) and 0 <= c < len(g[0]):
            g[r][c] = color
    return g


def solve(grid):
    g = grid
    b = 7
    colors = Counter(v for row in g for v in row if v != b)
    frame = colors.most_common(1)[0][0]
    p = pts(g, frame)
    a, bb, c, d = box(p)
    tile = [[b] * 5 for _ in range(5)]
    paint(
        tile,
        {
            (r, z)
            for r in range(5)
            for z in range(5)
            if (r in (0, 4) and 0 < z < 4) or (z in (0, 4) and 0 < r < 4)
        },
        frame,
    )
    inside = {(r, z) for r in range(a + 1, bb) for z in range(c + 1, d) if g[r][z] != b}
    if inside:
        x, y, z, t = box(inside)
        if len(inside) == 1:
            tile[2][2] = g[x][z]
        else:
            for r, cc_ in inside:
                tile[1 + round((r - x) * 2 / max(1, y - x))][
                    1 + round((cc_ - z) * 2 / max(1, t - z))
                ] = g[r][cc_]
    o = [[b] * 15 for _ in range(15)]
    for off in (2, 8):
        for r, row in enumerate(tile):
            o[r + off][off : off + 5] = row
    return o
