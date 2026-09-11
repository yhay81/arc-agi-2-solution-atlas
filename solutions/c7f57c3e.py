from collections import Counter


def cp(g):
    return [row[:] for row in g]


def put(g, r, c, v):
    if 0 <= r < len(g) and 0 <= c < len(g[0]):
        g[r][c] = v


def bbox(cells):
    return (
        min((r for r, c in cells)),
        max((r for r, c in cells)),
        min((c for r, c in cells)),
        max((c for r, c in cells)),
    )


def bg(g):
    return Counter(v for row in g for v in row).most_common(1)[0][0]


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
    import functools
    import math

    g = [row[:] for row in g]
    background = bg(g)
    objects = components(g, background, True, False)
    records = []
    for obj in objects:
        blue = [p for p in obj if g[p[0]][p[1]] == 1]
        if not blue:
            continue
        a, b, c, d = bbox(obj)
        lengths = []
        for lines in (
            [[g[r][col] for col in range(c, d + 1)] for r in range(a, b + 1)],
            [[g[r][col] for r in range(a, b + 1)] for col in range(c, d + 1)],
        ):
            for line in lines:
                run = 0
                last = None
                for v in line + [None]:
                    if v == last:
                        run += 1
                    else:
                        if last is not None and last != background:
                            lengths.append(run)
                        last = v
                        run = 1
        scale = functools.reduce(math.gcd, lengths)
        top, _, left, _ = bbox(blue)
        pattern = tuple(
            sorted({((r - top) // scale, (col - left) // scale, g[r][col]) for r, col in obj})
        )
        records.append((obj, top, left, scale, pattern))
    patterns = list(set(rec[4] for rec in records))
    if len(patterns) != 2:
        raise ValueError("Expected two symbol variants")
    out = cp(g)
    for obj, top, left, scale, pattern in records:
        for r, c in obj:
            out[r][c] = background
    for obj, top, left, scale, pattern in records:
        other = next(p for p in patterns if p != pattern)
        for r, c, v in other:
            for dr in range(scale):
                for dc in range(scale):
                    put(out, top + r * scale + dr, left + c * scale + dc, v)
    return out
