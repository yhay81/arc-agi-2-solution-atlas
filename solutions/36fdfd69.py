def solve(grid):
    out = [row[:] for row in grid]
    h, w = len(grid), len(grid[0])
    marks = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 2]
    for i, p in enumerate(marks):
        for q in marks[i + 1 :]:
            if p[0] == q[0] or p[1] == q[1]:
                continue
            top, bottom = min(p[0], q[0]), max(p[0], q[0])
            left, right = min(p[1], q[1]), max(p[1], q[1])
            if (p[0], p[1]) not in ((top, left), (top, right), (bottom, left), (bottom, right)) or (
                q[0] == p[0] and q[1] == p[1]
            ):
                continue
            if any(grid[r][c] == 0 for r in range(top, bottom + 1) for c in range(left, right + 1)):
                continue
            for r in range(top, bottom + 1):
                for c in range(left, right + 1):
                    if grid[r][c] != 2:
                        out[r][c] = 4
    return out
