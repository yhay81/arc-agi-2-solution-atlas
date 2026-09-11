def solve(grid):
    red = [(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == 2]
    pairs = [
        (a, b) for i, a in enumerate(red) for b in red[i + 1 :] if a[0] == b[0] or a[1] == b[1]
    ]
    if len(pairs) != 1:
        raise ValueError("Expected one aligned pair defining the trunk")
    a, b = pairs[0]
    out = [row[:] for row in grid]
    if a[0] == b[0]:
        for c in range(min(a[1], b[1]), max(a[1], b[1]) + 1):
            out[a[0]][c] = 3
        for r, c in red:
            if not min(a[1], b[1]) <= c <= max(a[1], b[1]):
                raise ValueError("Point projects outside the trunk")
            for rr in range(min(r, a[0]), max(r, a[0]) + 1):
                out[rr][c] = 3
    else:
        for r in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
            out[r][a[1]] = 3
        for r, c in red:
            if not min(a[0], b[0]) <= r <= max(a[0], b[0]):
                raise ValueError("Point projects outside the trunk")
            for cc in range(min(c, a[1]), max(c, a[1]) + 1):
                out[r][cc] = 3
    for r, c in red:
        out[r][c] = 2
    return out
