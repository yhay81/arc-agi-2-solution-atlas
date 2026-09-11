def solve(grid):
    g = grid
    h, w = (len(g), len(g[0]))
    gray = [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == 5]
    header = max((r for r, c in gray)) + 1
    labels = []
    for v in g[0]:
        if v not in (0, 5) and v not in labels:
            labels.append(v)
    cols = sorted({c for r, c in gray})
    runs = []
    for c in cols:
        if not runs or c != runs[-1][-1] + 1:
            runs.append([])
        runs[-1].append(c)
    if len(runs) != len(labels):
        raise ValueError("Legend lengths differ")
    patterns = {
        color: [[color if g[r][c] == 5 else 0 for c in run] for r in range(header)]
        for color, run in zip(labels, runs)
    }
    spots = [(r, c) for r in range(header, h) for c in range(w) if g[r][c] != 0]
    top = min((r for r, c in spots))
    bottom = max((r for r, c in spots))
    left = min((c for r, c in spots))
    right = max((c for r, c in spots))
    ph, pw = (header, len(runs[0]))
    out = [[0] * ((right - left + 1) * pw) for _ in range((bottom - top + 1) * ph)]
    for r in range(top, bottom + 1):
        for c in range(left, right + 1):
            pattern = patterns[g[r][c]]
            for a in range(ph):
                for b in range(pw):
                    out[(r - top) * ph + a][(c - left) * pw + b] = pattern[a][b]
    return out
