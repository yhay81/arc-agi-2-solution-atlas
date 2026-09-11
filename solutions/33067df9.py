def solve(grid):
    g = grid
    small = [row[1::2] for row in g[1::2]]
    nr, nc = (len(small), len(small[0]))
    hr, wc = (24 // nr, 24 // nc)
    out = [[0] * 26 for _ in range(26)]
    runs = []
    for r, row in enumerate(small):
        c = 0
        while c < nc:
            end = c + 1
            while end < nc and row[end] == row[c]:
                end += 1
            if row[c]:
                runs.append((r, c, end, row[c]))
            c = end
    for r, c, end, color in runs:
        bottom = r + 1
        while (bottom, c, end, color) in runs:
            bottom += 1
        for a in range(2 + r * hr, bottom * hr):
            for b in range(2 + c * wc, end * wc):
                out[a][b] = color
    return out
