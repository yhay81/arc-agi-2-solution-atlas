def cp(g):
    return [row[:] for row in g]


def points(g, color):
    return [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color]


def solve(grid):
    g = grid
    g = cp(g)
    remaining = set(points(g, 3))
    groups = []
    while remaining:
        first = remaining.pop()
        obj = {first}
        queue = [first]
        for r, c in queue:
            near = {p for p in remaining if max(abs(p[0] - r), abs(p[1] - c)) <= 2}
            remaining -= near
            obj |= near
            queue += list(near)
        groups.append(obj)
    out = cp(g)
    for obj in groups:
        options = []
        for ar, ac in obj:
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                uv = [
                    ((r - ar) * dr + (c - ac) * dc, -(r - ar) * dc + (c - ac) * dr) for r, c in obj
                ]
                if (
                    all((u >= 0 and abs(v) == u for u, v in uv))
                    and any((v < 0 for u, v in uv))
                    and any((v > 0 for u, v in uv))
                ):
                    options.append((ar, ac, dr, dc, max((u for u, v in uv))))
        if len(options) != 1:
            raise ValueError(("Triangle orientation unclear", obj, options))
        ar, ac, dr, dc, depth = options[0]
        for u in range(1, depth + 1):
            for v in range(-u, u + 1):
                rr, cc = (ar + u * dr - v * dc, ac + u * dc + v * dr)
                if 0 <= rr < len(g) and 0 <= cc < len(g[0]) and (g[rr][cc] != 3):
                    out[rr][cc] = 8
    return out
