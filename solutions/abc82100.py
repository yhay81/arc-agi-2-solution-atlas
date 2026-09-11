def cp(g):
    return [row[:] for row in g]


def put(g, r, c, v):
    if 0 <= r < len(g) and 0 <= c < len(g[0]):
        g[r][c] = v


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
    out = cp(g)
    templates = components([[8 if v == 8 else 0 for v in row] for row in g], 0, True, True)
    rules = []
    keys = set()
    for obj in templates:
        shape = set(obj)
        found = []
        for r in range(h):
            for c in range(w):
                new = g[r][c]
                if new in (0, 8):
                    continue
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    r2, c2 = (r + dr, c + dc)
                    ar, ac = (r - dr, c - dc)
                    if not (0 <= r2 < h and 0 <= c2 < w and (0 <= ar < h) and (0 <= ac < w)):
                        continue
                    old = g[r2][c2]
                    if old in (0, 8, new) or not any(
                        (abs(rr - ar) <= 1 and abs(cc - ac) <= 1 for rr, cc in obj)
                    ):
                        continue
                    if (ar, ac) not in shape and g[ar][ac] != 0:
                        continue
                    found.append((old, new, ar, ac, dr, dc, r2, c2, r, c))
        if not found:
            raise ValueError("No instruction attached to cyan template")
        for old, new, ar, ac, dr, dc, r2, c2, r, c in found:
            selected = obj
            if len(found) > 1 and len({(abs(f[4]), abs(f[5])) for f in found}) == 1:
                selected = [(rr, cc) for rr, cc in obj if (cc == ac if dr else rr == ar)]
            rules.append((old, new, [(rr - ar, cc - ac) for rr, cc in selected]))
            keys |= {(r, c), (r2, c2)}
        keys |= shape
    for r, c in keys:
        out[r][c] = 0
    mapping = {}
    for old, new, shape in rules:
        if old in mapping and mapping[old] != (new, shape):
            raise ValueError("Conflicting substitution")
        mapping[old] = (new, shape)
    for r in range(h):
        for c in range(w):
            if (r, c) not in keys and g[r][c] in mapping:
                out[r][c] = 0
    for r in range(h):
        for c in range(w):
            if (r, c) in keys or g[r][c] not in mapping:
                continue
            new, shape = mapping[g[r][c]]
            for dr, dc in shape:
                put(out, r + dr, c + dc, new)
    return out
