def solve(grid):
    h, w = len(grid), len(grid[0])
    marks = [(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == 8]
    if len(marks) != 1 or sum(v != 0 for row in grid for v in row) != 1:
        return [row[:] for row in grid]
    cr, cc = marks[0]
    out = [[0] * w for _ in range(h)]
    out[cr][cc] = 8
    for direction in (-1, 1):
        row, distance = cr + direction, 1
        while 0 <= row < h:
            steps = distance // 2
            col = cc - direction * 2 * steps
            if distance % 2:
                cols = (col,)
            else:
                other = cc - direction * 2 * (steps - 1)
                cols = range(min(col, other), max(col, other) + 1)
            for c in cols:
                if 0 <= c < w:
                    out[row][c] = 5
            distance += 1
            row += direction
    return out
