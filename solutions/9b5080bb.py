from collections import Counter


def cp(g):
    return [row[:] for row in g]


def bbox(cells):
    return (
        min((r for r, c in cells)),
        max((r for r, c in cells)),
        min((c for r, c in cells)),
        max((c for r, c in cells)),
    )


def components(g, background=0, diagonal=False, mono=True):
    unseen = {(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v != background}
    out = []
    while unseen:
        p = min(unseen)
        unseen.remove(p)
        q = [p]
        cells = []
        for r, c in q:
            cells.append((r, c))
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if not (dr or dc) or (not diagonal and dr and dc):
                        continue
                    n = (r + dr, c + dc)
                    if n in unseen and (not mono or g[n[0]][n[1]] == g[r][c]):
                        unseen.remove(n)
                        q.append(n)
        out.append(cells)
    return out


def solve(grid):
    g = grid
    h, w = (len(g), len(g[0]))
    border = g[0] + g[-1] + [row[0] for row in g] + [row[-1] for row in g]
    base = Counter(border).most_common(1)[0][0]
    allcolors = set(sum(g, []))
    scores = Counter()
    for color in allcolors - {base}:
        for obj in components(
            [[v if v == color else -1 for v in row] for row in g], -1, False, True
        ):
            a, b, c, d = bbox(obj)
            if b - a >= 2 and d - c >= 2 and (len(obj) / ((b - a + 1) * (d - c + 1)) >= 0.75):
                holes = components(
                    [
                        [1 if g[r][col] != color else 0 for col in range(c, d + 1)]
                        for r in range(a, b + 1)
                    ],
                    0,
                    False,
                    True,
                )
                if not any(
                    all((r not in (0, b - a) and col not in (0, d - c) for r, col in hole))
                    for hole in holes
                ):
                    scores[color] += len(obj)
    main = scores.most_common(1)[0][0]
    fields = allcolors - {base, main}
    if len(fields) != 2:
        raise ValueError("Expected two surrounding fields")
    out = cp(g)
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for obj in components([[v if v == main else -1 for v in row] for row in g], -1, False, True):
        core_rows = Counter((r for r, col in obj))
        core_cols = Counter((col for r, col in obj))
        core = (
            min((r for r, n in core_rows.items() if n >= 2)),
            max((r for r, n in core_rows.items() if n >= 2)),
            min((col for col, n in core_cols.items() if n >= 2)),
            max((col for col, n in core_cols.items() if n >= 2)),
        )
        boundary = Counter(
            (
                g[r + dr][c + dc]
                for r, c in obj
                for dr, dc in dirs
                if 0 <= r + dr < h and 0 <= c + dc < w and (g[r + dr][c + dc] in fields)
            )
        )
        field = boundary.most_common(1)[0][0]
        other = (fields - {field}).pop()
        a, b, c, d = bbox(obj)
        for r in range(max(1, a - 1), min(h - 1, b + 2)):
            for col in range(max(1, c - 1), min(w - 1, d + 2)):
                neighbors = [(r + dr, col + dc) for dr, dc in dirs]
                inside = [p for p in neighbors if g[p[0]][p[1]] == main]
                if (
                    g[r][col] == main
                    and len(inside) == 1
                    and (not (core[0] <= r <= core[1] and core[2] <= col <= core[3]))
                ):
                    out[r][col] = other
                    out[inside[0][0]][inside[0][1]] = other
                elif g[r][col] == field and len(inside) == 3:
                    q = next(p for p in neighbors if p not in inside)
                    out[r][col] = other
                    out[q[0]][q[1]] = other
    return out
