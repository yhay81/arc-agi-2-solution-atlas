def copy(g):
    return [r[:] for r in g]


def solve(grid):
    g = grid
    g = copy(g)
    seps = [r for r, row in enumerate(g) if all(v == 5 for v in row)]
    bounds = [-1] + seps + [len(g)]
    frames = [g[a + 1 : b] for a, b in zip(bounds, bounds[1:])]
    prev, last = frames[-2:]
    out = copy(last)
    changes = [
        (r, c, prev[r][c], last[r][c])
        for r in range(len(last))
        for c in range(len(last[0]))
        if prev[r][c] != last[r][c]
    ]
    if changes and all((x and y for r, c, x, y in changes)):
        old, new = changes[0][2:]
        cols = [c for r, c, x, y in changes]
        target = max(cols) + 1
        for r, row in enumerate(out):
            if target < len(row) and row[target] == old:
                row[target] = new
        return out
    counts = [sum(v != 0 for row in p for v in row) for p in frames]
    if len(set(counts)) == 1:
        ps1 = [(r, c, v) for r, row in enumerate(prev) for c, v in enumerate(row) if v]
        ps2 = [(r, c, v) for r, row in enumerate(last) for c, v in enumerate(row) if v]
        dr, dc = (ps2[0][0] - ps1[0][0], ps2[0][1] - ps1[0][1])
        out = [[0] * len(last[0]) for _ in last]
        for r, c, v in ps2:
            if 0 <= r + dr < len(out) and 0 <= c + dc < len(out[0]):
                out[r + dr][c + dc] = v
    else:
        added = [(r, c, y) for r, c, x, y in changes if not x and y]
        delta = len(added)
        row = max(range(len(last)), key=lambda r: sum(bool(v) for v in last[r]))
        positions = [c for c, v in enumerate(last[row]) if v]
        color = last[row][positions[-1]]
        for c in range(max(positions) + 1, min(len(out[0]), max(positions) + delta + 1)):
            out[row][c] = color
    return out
