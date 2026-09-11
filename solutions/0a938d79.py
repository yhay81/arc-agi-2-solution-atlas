def _repeat_two_marker_lines(grid):
    height = len(grid)
    width = len(grid[0]) if height else 0
    positions = [(r, c) for r in range(height) for c in range(width) if grid[r][c]]
    if len(positions) != 2:
        return [row[:] for row in grid]
    output = [[0] * width for _ in range(height)]
    if height >= width:
        rows = sorted({int(row) for row, _ in positions})
        if len(rows) != 2:
            return [row[:] for row in grid]
        first, second = rows
        period = second - first
        if period <= 0:
            return [row[:] for row in grid]
        first_col = next(c for c in range(width) if grid[first][c])
        second_col = next(c for c in range(width) if grid[second][c])
        first_color = grid[first][first_col]
        second_color = grid[second][second_col]
        for row in range(first, height, period):
            color = first_color if (row - first) // period % 2 == 0 else second_color
            output[row] = [color] * width
    else:
        cols = sorted({int(col) for _, col in positions})
        if len(cols) != 2:
            return [row[:] for row in grid]
        first, second = cols
        period = second - first
        if period <= 0:
            return [row[:] for row in grid]
        first_row = next(r for r in range(height) if grid[r][first])
        second_row = next(r for r in range(height) if grid[r][second])
        first_color = grid[first_row][first]
        second_color = grid[second_row][second]
        for col in range(first, width, period):
            color = first_color if (col - first) // period % 2 == 0 else second_color
            for row in output:
                row[col] = color
    return output


def solve(grid):
    return _repeat_two_marker_lines(grid)
