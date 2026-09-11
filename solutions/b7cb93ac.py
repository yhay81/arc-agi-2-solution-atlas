import json as json


def bbox(ps):
    return (
        min((r for r, c in ps)),
        min((c for r, c in ps)),
        max((r for r, c in ps)),
        max((c for r, c in ps)),
    )


def copy(g):
    return [r[:] for r in g]


def components(g, background=None, by_color=True, diagonal=False):
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    if diagonal:
        offsets += [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    h, w = (len(g), len(g[0]))
    unseen = {(r, c) for r in range(h) for c in range(w) if g[r][c] != background}
    result = []
    while unseen:
        start = min(unseen)
        unseen.remove(start)
        queue = [start]
        cells = []
        color = g[start[0]][start[1]]
        while queue:
            r, c = queue.pop()
            cells.append((r, c))
            for dr, dc in offsets:
                p = (r + dr, c + dc)
                if p in unseen and (not by_color or g[p[0]][p[1]] == color):
                    unseen.remove(p)
                    queue.append(p)
        result.append((color, cells))
    return result


def solve(grid):
    g = grid
    groups = sorted(components(g, background=0), key=lambda p: -len(p[1]))
    pieces = []
    for j, (color, ps) in enumerate(groups):
        variants = set()
        points = ps
        for k in range(1 if j == 0 else 4):
            a, b, z, d = bbox(points)
            variants.add(tuple(sorted(((r - a, c - b) for r, c in points))))
            points = [(c, -r) for r, c in points]
        pieces.append((color, variants))
    area = sum((len(ps) for col, ps in groups))
    solutions = []
    for h in range(2, int(area**0.5) + 1):
        if area % h:
            continue
        w = area // h

        def search(j, out):
            if j == len(pieces):
                solutions.append(out)
                return
            color, variants = pieces[j]
            for shape in variants:
                ph = max((r for r, c in shape)) + 1
                pw = max((c for r, c in shape)) + 1
                for a in range(h - ph + 1):
                    for b in range(w - pw + 1):
                        if all((out[a + r][b + c] == 0 for r, c in shape)):
                            nxt = copy(out)
                            for r, c in shape:
                                nxt[a + r][b + c] = color
                            search(j + 1, nxt)

        search(0, [[0] * w for _ in range(h)])
    unique = {json.dumps(x): x for x in solutions}
    if not unique:
        raise ValueError("no fill solution exists")

    def score(out):
        colors = sorted({v for row in out for v in row})
        old = {
            v: sum((c for r, row in enumerate(g) for c, x in enumerate(row) if x == v))
            / sum(x == v for row in g for x in row)
            for v in colors
        }
        new = {
            v: sum((c for r, row in enumerate(out) for c, x in enumerate(row) if x == v))
            / sum(x == v for row in out for x in row)
            for v in colors
        }
        return sum(
            (old[x] - old[y]) * (new[x] - new[y]) > 0 for x in colors for y in colors if x < y
        )

    ranked = sorted(unique.values(), key=score, reverse=True)
    if len(ranked) > 1 and score(ranked[0]) == score(ranked[1]):
        raise ValueError("solution is not unique even after applying the left-right relation")
    return ranked[0]
