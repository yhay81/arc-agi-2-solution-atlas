def cp(g):
    return [row[:] for row in g]


def points(g, color):
    return [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    yellow = set(points(g, 4))
    reds = set(points(g, 2))
    groups = []
    for r in range(len(g) - 2):
        for c in range(len(g[0]) - 2):
            corners = {(r, c), (r, c + 2), (r + 2, c), (r + 2, c + 2)}
            present = corners & yellow
            if len(present) == 3:
                missing = next(iter(corners - present))
                sr = 1 if missing[0] == r else -1
                sc = 1 if missing[1] == c else -1
                groups.append((present, missing, sr, sc))
    if not groups:
        raise ValueError("No three-corner markers")
    source = min(groups, key=lambda x: min((abs(x[1][0] - r) + abs(x[1][1] - c) for r, c in reds)))
    _, anchor, sr, sc = source
    pattern = {((r - anchor[0]) * sr, (c - anchor[1]) * sc) for r, c in reds}
    out = cp(g)
    if len(pattern) == 8:
        for u, v in ((-2, -1), (-1, -2)):
            pattern.discard((u, v))
            rr = anchor[0] + u * sr
            cc = anchor[1] + v * sc
            if out[rr][cc] == 2:
                out[rr][cc] = 0
    for present, missing, tr, tc in groups:
        if present == source[0]:
            continue
        for u, v in pattern:
            r = missing[0] + u * tr
            c = missing[1] + v * tc
            if not (0 <= r < len(g) and 0 <= c < len(g[0])):
                raise ValueError("Copied pattern leaves grid")
            if out[r][c] == 0:
                out[r][c] = 2
    return out
