def solve(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    for row in range(height):
        for col in range(width):
            if grid[row][col] != 5:
                continue
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    target_row, target_col = row + dr, col + dc
                    if 0 <= target_row < height and 0 <= target_col < width:
                        output[target_row][target_col] = 5 if dr and dc else int(bool(dr or dc))
    return output
