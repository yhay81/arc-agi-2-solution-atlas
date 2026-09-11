def components(grid):
    h, w = len(grid), len(grid[0])
    unseen = {(r, c) for r in range(h) for c in range(w) if grid[r][c]}
    out = []
    while unseen:
        todo = [unseen.pop()]
        cells = []
        while todo:
            r, c = todo.pop()
            cells.append((r, c))
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                p = r + dr, c + dc
                if p in unseen:
                    unseen.remove(p)
                    todo.append(p)
        out.append(cells)
    return out


def solve(grid):
    a = grid
    h, w = len(a), len(a[0])
    out = [[4] * w for _ in range(h)]
    for ps in components([[v == 1 for v in row] for row in a]):
        r, c = min(x for x, _ in ps), min(y for _, y in ps)
        b, d = max(x for x, _ in ps), max(y for _, y in ps)
        full = len(ps) == (b - r + 1) * (d - c + 1)
        inside = {(x, y) for x, y in ps}
        boundary = {
            (x, y) for x in range(r, b + 1) for y in range(c, d + 1) if x in (r, b) or y in (c, d)
        } - inside
        seen = set(boundary)
        todo = list(boundary)
        while todo:
            x, y = todo.pop()
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                q = x + dx, y + dy
                if r <= q[0] <= b and c <= q[1] <= d and q not in inside and q not in seen:
                    seen.add(q)
                    todo.append(q)
        closed = full or any(
            (x, y) not in seen
            for x in range(r, b + 1)
            for y in range(c, d + 1)
            if (x, y) not in inside
        )
        color, shift = (2, -c) if closed else (3, w - 1 - d)
        for x, y in ps:
            out[x][y + shift] = color
    return out
