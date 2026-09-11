def solve(grid):
    source = [list(row) for row in grid]
    output = [row[:] for row in source]
    cells = [
        (r, c) for r, row in enumerate(source) for c, value in enumerate(row) if value in (1, 9)
    ]
    top = min(r for r, _ in cells)
    left = min(c for _, c in cells)
    block = [row[left : left + 3] for row in source[top : top + 3]]
    for r in range(top, top + 3):
        output[r][left : left + 3] = [7] * 3

    for offset, column in enumerate(zip(*block)):
        col = left + offset
        obstacles = [r - (top + 3) for r in range(top + 3, len(source)) if source[r][col] == 5]
        bottom = top + 3 + obstacles[0] if 1 in column and obstacles else len(source)
        for i, value in enumerate(column):
            output[bottom - 3 + i][col] = value
    return output
