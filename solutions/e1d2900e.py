def solve(grid):
    a = grid
    a = [row[:] for row in a]
    h, w = len(a), len(a[0])
    squares = [
        (r, c)
        for r in range(h - 1)
        for c in range(w - 1)
        if all(a[y][x] == 2 for y in (r, r + 1) for x in (c, c + 1))
    ]
    out = [row[:] for row in a]
    blues = [(r, c) for r, row in enumerate(a) for c, v in enumerate(row) if v == 1]
    for r, c in blues:
        out[r][c] = 0
    for row, col in blues:

        def distance(square):
            r, c = square
            return max(max(r - row, 0, row - (r + 1)), max(c - col, 0, col - (c + 1)))

        sr, sc = min(squares, key=distance)
        if sr <= row <= sr + 1:
            target = (row, sc - 1 if col < sc else sc + 2)
        elif sc <= col <= sc + 1:
            target = (sr - 1 if row < sr else sr + 2, col)
        else:
            target = (row, col)
        out[target[0]][target[1]] = 1
    return out
