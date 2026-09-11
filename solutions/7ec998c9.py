from collections import Counter


def cp(g):
    return [row[:] for row in g]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    h, w = (len(g), len(g[0]))
    counts = Counter(v for row in g for v in row)
    background = counts.most_common(1)[0][0]
    marks = [(r, c, g[r][c]) for r in range(h) for c in range(w) if g[r][c] != background]
    if len(marks) != 1:
        raise ValueError("The colored pivot is not unique")
    r, c, color = marks[0]
    out = cp(g)
    for rr in range(h):
        if rr != r:
            out[rr][c] = 1
    if color in (4, 9):
        for cc in range(c):
            out[0][cc] = 1
        for cc in range(c + 1, w):
            out[h - 1][cc] = 1
    elif color in (6, 8):
        for cc in range(c + 1, w):
            out[0][cc] = 1
        for cc in range(c):
            out[h - 1][cc] = 1
    else:
        raise ValueError("Unknown pivot color")
    return out
