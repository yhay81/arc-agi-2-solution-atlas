def solve(grid):
    g = grid
    g = [row[:] for row in g]
    out = [r[:] for r in g]
    blues = [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == 1]
    purple = [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == 6]
    if len(purple) != len(blues):
        raise ValueError("Expected one blue pivot per purple point")
    matches = []

    def match(remaining, available, assigned):
        if len(matches) > 1:
            return
        if not remaining:
            matches.append(assigned)
            return
        p = min(remaining, key=lambda p: sum((a == p[0] or b == p[1] for a, b in available)))
        for pivot in sorted(available):
            if pivot[0] == p[0] or pivot[1] == p[1]:
                match(remaining - {p}, available - {pivot}, assigned + [(p, pivot)])

    match(set(purple), set(blues), [])
    if len(matches) != 1:
        raise ValueError("Expected unique aligned one-to-one matching")
    for r, c in purple:
        out[r][c] = 8
    for (r, c), (a, b) in matches[0]:
        nr, nc = (a - (c - b), b + (r - a))
        if 0 <= nr < len(g) and 0 <= nc < len(g[0]):
            out[nr][nc] = 7
    return out
