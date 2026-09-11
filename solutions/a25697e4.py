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


def bg(g):
    return Counter(v for row in g for v in row).most_common(1)[0][0]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    h, w = (len(g), len(g[0]))
    base = bg(g)
    objs = components(g, base, True, False)
    parts = [
        o
        for o in objs
        if len({g[r][c] for r, c in o}) == 1
        and any((r in (0, h - 1) or c in (0, w - 1) for r, c in o))
    ]
    groups = {}
    for o in parts:
        edge = next(
            e for e in range(4) if any(([r == 0, r == h - 1, c == 0, c == w - 1][e] for r, c in o))
        )
        groups.setdefault((g[o[0][0]][o[0][1]], edge), []).extend(o)
    locks = list(groups.values())
    keys = [o for o in objs if o not in parts]
    fixed = {p for o in locks for p in o}
    options = []
    for lock in locks:
        a, b, c, d = bbox(lock)
        hole = {
            (r, col) for r in range(a, b + 1) for col in range(c, d + 1) if (r, col) not in lock
        }
        anchor = min(hole)
        candidates = []
        for ki, key in enumerate(keys):
            colors = {g[r][col] for r, col in key}
            shape = {(r, col): g[r][col] for r, col in key}
            for orientation in range(8):
                if orientation == 4:
                    shape = {(r, -col): g[r][col] for r, col in key}
                for sr, sc in shape:
                    dr, dc = (anchor[0] - sr, anchor[1] - sc)
                    moved = {(r + dr, col + dc): v for (r, col), v in shape.items()}
                    if (
                        not hole <= set(moved)
                        or fixed & set(moved)
                        or any((r < 0 or r >= h or col < 0 or (col >= w) for r, col in moved))
                    ):
                        continue
                    innercolors = {moved[p] for p in hole}
                    if len(innercolors) != 1:
                        continue
                    inner = next(iter(innercolors))
                    outer = next(v for v in colors if v != inner)
                    paint = {
                        p: (outer if p in hole else inner)
                        if orientation >= 4
                        else inner
                        if p in hole
                        else outer
                        for p in moved
                    }
                    candidates.append((ki, paint))
                shape = {(col, -r): v for (r, col), v in shape.items()}
        options.append(candidates)
    solutions = []

    def search(i, used, paint):
        if len(solutions) > 1:
            return
        if i == len(options):
            result = tuple(sorted(paint.items()))
            if result not in solutions:
                solutions.append(result)
            return
        for ki, p in options[i]:
            if ki not in used and (not set(p) & set(paint)):
                search(i + 1, used | {ki}, {**paint, **p})

    search(0, set(), {})
    if len(solutions) != 1:
        raise ValueError(f"Expected unique key placement: {len(solutions)}")
    out = cp(g)
    for o in keys:
        for r, c in o:
            out[r][c] = base
    for (r, c), v in solutions[0]:
        out[r][c] = v
    return out
