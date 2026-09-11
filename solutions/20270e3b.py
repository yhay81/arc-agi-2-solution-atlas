def components(grid, color):
    h, w = len(grid), len(grid[0])
    unseen = {(r, c) for r in range(h) for c in range(w) if grid[r][c] == color}
    out = []
    while unseen:
        s = unseen.pop()
        q = [s]
        cells = []
        for r, c in q:
            cells.append((r, c))
            for p in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if p in unseen:
                    unseen.remove(p)
                    q.append(p)
        out.append(cells)
    return out


def solve(grid):
    a = grid
    h0, w0 = len(a), len(a[0])
    active = {(r, c) for r in range(h0) for c in range(w0) if a[r][c] != 1}
    marks = components(a, 7)
    if not (len(marks) == 2):
        raise ValueError("task assumptions are not satisfied")
    choices = []
    for base, other in (marks, marks[::-1]):
        seen = set(base)
        todo = list(seen)
        while todo:
            r, c = todo.pop()
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    q = (r + dr, c + dc)
                    if (dr or dc) and q in active and q not in seen:
                        seen.add(q)
                        todo.append(q)
        dy = min(r for r, c in base) - min(r for r, c in other) - 1
        dx = min(c for r, c in base) - min(c for r, c in other)
        shifted = {(r + dy, c + dx) for r, c in active - seen}
        merged = seen | shifted
        if min(r for r, c in merged) < 0 or min(c for r, c in merged) < 0:
            continue
        hh = max(r for r, c in merged) + 1
        ww = max(c for r, c in merged) + 1
        choices.append((hh * ww, hh, ww, merged))
    _, h, w, merged = min(choices, key=lambda t: t[:3])
    out = [[1] * w for _ in range(h)]
    for r, c in merged:
        out[r][c] = 4
    return out
