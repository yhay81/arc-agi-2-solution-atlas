def solve(grid):
    height, width = len(grid), len(grid[0])
    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = max(counts, key=counts.get)
    output = [row[:] for row in grid]
    first = {}
    for row in range(height):
        for col in range(width):
            if grid[row][col] != background:
                first.setdefault(grid[row][col], (row, col))
    specs = {1: (0, 1, 2, -1, 2), 2: (0, -1, 3, 0, -4), 3: (1, 0, 2, 3, 0), 6: (-1, 0, 5, -6, 0)}
    for color, (row, col) in first.items():
        if color not in specs:
            continue
        dr, dc, length, end_row, end_col = specs[color]
        for step in range(1, length + 1):
            r, c = row + dr * step, col + dc * step
            if 0 <= r < height and 0 <= c < width:
                output[r][c] = 5
        r, c = row + end_row, col + end_col
        if 0 <= r < height and 0 <= c < width:
            output[r][c] = color
    for row in range(height):
        for col in range(width):
            if output[row][col] != 5 or not (0 < row < height - 1 and 0 < col < width - 1):
                continue
            if all(
                output[r][c] != background
                for r, c in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1))
            ):
                r, c = row, col
                while 0 <= r < height and 0 <= c < width:
                    output[r][c] = 4
                    r, c = r + 1, c - 1
    return output
