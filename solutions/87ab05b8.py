def _marker_quadrant_block(grid):
    positions = [(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == 2]
    height, width = len(grid), len(grid[0])
    if len(positions) != 1 or height % 2 or width % 2:
        return [row[:] for row in grid]
    counts = [sum(value == color for row in grid for value in row) for color in range(10)]
    background = max(range(10), key=lambda color: (counts[color], -color))
    output = [[background] * width for _ in range(height)]
    row, col = positions[0]
    half_rows, half_cols = height // 2, width // 2
    top = 0 if row < half_rows else half_rows
    left = 0 if col < half_cols else half_cols
    for r in range(top, top + half_rows):
        for c in range(left, left + half_cols):
            output[r][c] = 2
    return output


def solve(grid):
    return _marker_quadrant_block(grid)
