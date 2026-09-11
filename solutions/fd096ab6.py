from collections import Counter


def bbox(ps):
    return (
        min((r for r, c in ps)),
        min((c for r, c in ps)),
        max((r for r, c in ps)),
        max((c for r, c in ps)),
    )


def copy(g):
    return [r[:] for r in g]


def bg(g):
    return Counter(v for row in g for v in row).most_common(1)[0][0]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    back = bg(g)
    template = [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == 4]
    a, b, z, d = bbox(template)
    shape = {(r - a, c - b) for r, c in template}
    out = copy(g)
    groups = []
    for color in set(v for row in g for v in row) - {back, 4}:
        unseen = {(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color}
        while unseen:
            cs = [unseen.pop()]
            q = cs[:]
            while q:
                p = q.pop()
                near = [
                    v
                    for v in unseen
                    if max(abs(p[0] - v[0]), abs(p[1] - v[1])) <= max(z - a, d - b)
                ]
                for v in near:
                    unseen.remove(v)
                    cs.append(v)
                    q.append(v)
            groups.append((color, cs))
    for color, cs in groups:
        ps = set(cs)
        candidates = []
        for r in range(-z + a, len(g)):
            for c in range(-d + b, len(g[0])):
                cells = {(r + x, c + y) for x, y in shape}
                if ps <= cells and all(
                    (
                        0 <= x < len(g) and 0 <= y < len(g[0]) and (g[x][y] in (back, color))
                        for x, y in cells
                    )
                ):
                    candidates.append(cells)
        if len(candidates) != 1:
            raise ValueError(
                f"subshape color {color} has placement candidate count {len(candidates)}"
            )
        for r, c in candidates[0]:
            out[r][c] = color
    return out
