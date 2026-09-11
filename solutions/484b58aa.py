def solve(grid):
    h, w = len(grid), len(grid[0])
    marked = [
        (row, col, value)
        for row, line in enumerate(grid)
        for col, value in enumerate(line)
        if value
    ]
    periods = sorted(
        ((rows * cols, rows, cols) for rows in range(1, h + 1) for cols in range(1, w + 1)),
        key=lambda item: (item[0], item[1]),
    )
    for _, rows, cols in periods:
        if rows == h and cols == w:
            continue
        pattern = {}
        for row, col, value in marked:
            position = row % rows, col % cols
            if position in pattern and pattern[position] != value:
                break
            pattern[position] = value
        else:
            output = [
                [pattern.get((row % rows, col % cols), 0) for col in range(w)] for row in range(h)
            ]
            if any(
                grid[row][col] == 0 and output[row][col] for row in range(h) for col in range(w)
            ):
                return output
    return [row[:] for row in grid]
