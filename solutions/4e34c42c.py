from collections import Counter


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
    background = bg(g)
    objects = components(g, background, True, False)
    parts = []
    for o in objects:
        a, b, c, d = bbox(o)
        member = set(o)
        parts.append(
            {
                (r, col): g[r][col] if (r, col) in member else background
                for r in range(a, b + 1)
                for col in range(c, d + 1)
            }
        )

    def ccsets(part):
        pending = {p for p, v in part.items() if v != background}
        result = []
        while pending:
            seed = pending.pop()
            seen = {seed}
            queue = [seed]
            for r, c in queue:
                for q in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if q in pending and part[q] == part[seed]:
                        pending.remove(q)
                        seen.add(q)
                        queue.append(q)
            result.append(frozenset(seen))
        return set(result)

    while len(parts) > 1:
        choices = []
        groups = [ccsets(p) for p in parts]
        for i, A in enumerate(parts):
            for j in range(i + 1, len(parts)):
                B = parts[j]
                shifts = {
                    (r - a, c - b)
                    for (r, c), v in A.items()
                    for (a, b), u in B.items()
                    if v == u and v != background
                }
                for dr, dc in shifts:
                    shifted = {(r + dr, c + dc): v for (r, c), v in B.items()}
                    overlap = set(A) & set(shifted)
                    score = sum(A[p] != background for p in overlap)
                    if score < 2 or any(A[p] != shifted[p] for p in overlap):
                        continue
                    shiftedgroups = {
                        frozenset(((r + dr, c + dc) for r, c in group)) for group in groups[j]
                    }
                    complete = bool(groups[i] & shiftedgroups)
                    choices.append((complete, score, i, j, dr, dc))
        if not choices:
            raise ValueError("No consistent matching joint")
        _, _, i, j, dr, dc = max(choices)
        parts[i].update({(r + dr, c + dc): v for (r, c), v in parts[j].items()})
        parts.pop(j)
    final = {p: v for p, v in parts[0].items() if v != background}
    a, b, c, d = bbox(final)
    out = [[background] * (d - c + 1) for _ in range(b - a + 1)]
    for (r, col), v in final.items():
        out[r - a][col - c] = v
    return out
