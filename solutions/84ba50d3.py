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
                p = (r + dr, c + dc)
                if p in unseen:
                    unseen.remove(p)
                    todo.append(p)
        out.append(cells)
    return out


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    barrier = next(r for r, row in enumerate(a) if all(v == 2 for v in row))
    out = [[8 if v == 1 else v for v in row] for row in a]
    for ps in components([[v == 1 for v in row] for row in a]):
        rows = [r for r, _ in ps]
        wide = [r for r in set(rows) if rows.count(r) >= 2]
        shift = barrier - 1 - max(wide) if wide else len(a) - 1 - max(rows)
        for n in range(1, shift + 1):
            for r, c in ps:
                if a[r + n][c] == 2:
                    out[r + n][c] = 8
        for r, c in ps:
            out[r + shift][c] = 1
    return out
