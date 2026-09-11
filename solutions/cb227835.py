def solve(grid):
    h, w = len(grid), len(grid[0])
    marker_color = 8
    path_color = 3
    points = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == marker_color]
    if len(points) != 2 or marker_color == path_color:
        return [row[:] for row in grid]
    first, second = points
    if (second[0], second[1]) < (first[0], first[1]):
        first, second = (second, first)
    r0, c0 = first
    r1, c1 = second
    dr, dc = (abs(r1 - r0), abs(c1 - c0))
    sr = 1 if r1 >= r0 else -1
    sc = 1 if c1 >= c0 else -1
    output = [row[:] for row in grid]

    def paint(row: int, col: int) -> None:
        if (row, col) in (first, second):
            return
        if 0 <= row < h and 0 <= col < w and output[row][col] == 0:
            output[row][col] = path_color

    if dr >= dc:
        excess = dr - dc
        for step in range(dr + 1):
            row = r0 + sr * step
            if step <= dc:
                paint(row, c0 + sc * step)
            if step <= excess:
                paint(row, c0)
            from_second = dr - step
            row = r1 - sr * from_second
            if from_second <= dc:
                paint(row, c1 - sc * from_second)
            if from_second <= excess:
                paint(row, c1)
    else:
        excess = dc - dr
        for step in range(dc + 1):
            col = c0 + sc * step
            if step <= dr:
                paint(r0 + sr * step, col)
            if step <= excess:
                paint(r0, col)
            from_second = dc - step
            col = c1 - sc * from_second
            if from_second <= dr:
                paint(r1 - sr * from_second, col)
            if from_second <= excess:
                paint(r1, col)
    return output
