from collections import Counter


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
    background = bg(g)
    out = [[background if v == 2 else v for v in row] for row in g]
    red = components(
        [[2 if v == 2 else background for v in row] for row in g], background, False, True
    )
    forks = components(
        [[background if v == 2 else v for v in row] for row in g], background, False, True
    )
    for obj in forks:
        choices = []
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            uv = {(r * dr + c * dc, -r * dc + c * dr) for r, c in obj}
            us = [u for u, v in uv]
            vs = [v for u, v in uv]
            base = min(us)
            end = max(us)
            if not all((base, v) in uv for v in range(min(vs), max(vs) + 1)):
                continue
            profile = {v: max((u for u, vv in uv if vv == v)) for v in set(vs)}
            middle = [v for v, u in profile.items() if base < u < end]
            if not middle or max(middle) - min(middle) + 1 != len(middle):
                continue
            tip = {profile[v] for v in middle}
            if len(tip) != 1:
                continue
            choices.append((dr, dc, min(middle), max(middle), tip.pop()))
        if len(choices) != 1:
            raise ValueError("Fork direction is not unique")
        dr, dc, lo, hi, tip = choices[0]
        matches = []
        for block in red:
            uv = [(r * dr + c * dc, -r * dc + c * dr) for r, c in block]
            us = [u for u, v in uv]
            vs = [v for u, v in uv]
            if min(vs) == lo and max(vs) == hi and (min(us) > tip):
                matches.append((min(us), max(us), block))
        if not matches:
            continue
        start, stop, block = min(matches, key=lambda x: x[0])
        depth = stop - start + 1
        for u in range(tip + 1, stop + 1):
            for v in range(lo, hi + 1):
                r = u * dr - v * dc
                c = u * dc + v * dr
                out[r][c] = 2 if u <= tip + depth else 0
    return out
