def _connect_diagonal_markers(array):
    output = [row[:] for row in array]
    for color in {value for row in array for value in row if value != 0}:
        points = [
            (r, c) for r, row in enumerate(array) for c, value in enumerate(row) if value == color
        ]
        if len(points) != 2:
            continue
        (r0, c0), (r1, c1) = points
        dr, dc = r1 - r0, c1 - c0
        if abs(dr) != abs(dc) or dr == 0:
            continue
        step_r, step_c = (1 if dr > 0 else -1, 1 if dc > 0 else -1)
        for offset in range(abs(dr) + 1):
            output[r0 + offset * step_r][c0 + offset * step_c] = color
    return output


def solve(grid):
    return _connect_diagonal_markers(grid)
