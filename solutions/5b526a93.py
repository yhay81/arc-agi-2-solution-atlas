def solve(grid):
    a = grid
    a = [row[:] for row in a]
    centers = []
    for r in range(1, len(a) - 1):
        for c in range(1, len(a[0]) - 1):
            neighbors = [
                a[rr][cc]
                for rr in range(r - 1, r + 2)
                for cc in range(c - 1, c + 2)
                if (rr, cc) != (r, c)
            ]
            if a[r][c] == 0 and all(v == 1 for v in neighbors):
                centers.append((r, c))
    out = [row[:] for row in a]
    for r in sorted({p[0] for p in centers}):
        for c in sorted({p[1] for p in centers}):
            if (r, c) not in centers:
                for rr in range(r - 1, r + 2):
                    for cc in range(c - 1, c + 2):
                        out[rr][cc] = 8
                out[r][c] = 0
    return out
