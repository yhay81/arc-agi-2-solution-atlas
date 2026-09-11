def solve(grid):
    h, w = len(grid), len(grid[0])
    pts = [(r, c) for r in range(h) for c in range(w) if grid[r][c]]
    if not pts:
        return [r[:] for r in grid]
    t, l = min(r for r, _ in pts), min(c for _, c in pts)
    b, q = max(r for r, _ in pts), max(c for _, c in pts)
    crop = [row[l : q + 1] for row in grid[t : b + 1]]

    def runs(lines):
        out = []
        start = 0
        for i in range(1, len(lines)):
            if lines[i] != lines[i - 1]:
                out.append((start, i))
                start = i
        out.append((start, len(lines)))
        return out

    rr, cc = runs(crop), runs([[crop[i][j] for i in range(len(crop))] for j in range(len(crop[0]))])
    if len(rr) < 2 or len(cc) < 2:
        return [r[:] for r in grid]
    out = []
    for a, z in rr:
        line = []
        for c, d in cc:
            vals = {crop[i][j] for i in range(a, z) for j in range(c, d)}
            if len(vals) != 1 or 0 in vals:
                return [r[:] for r in grid]
            line.append(next(iter(vals)))
        out.append(line)
    return out
