def solve(grid):
    g = grid
    g = [row[:] for row in g]
    h, w = (len(g) // 3, len(g[0]) // 3)
    out = []
    for i in range(3):
        row = []
        for j in range(3):
            colors = [
                g[r][c]
                for r in range(i * h, (i + 1) * h)
                for c in range(j * w, (j + 1) * w)
                if g[r][c]
            ]
            if len(colors) != 1:
                raise ValueError("each third does not contain exactly one point")
            row.append(colors[0])
        out.append(row)
    return out
