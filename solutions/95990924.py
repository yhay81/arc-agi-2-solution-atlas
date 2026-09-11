def solve(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    for row in range(height - 1):
        for col in range(width - 1):
            if all(grid[row + dr][col + dc] == 5 for dr in (0, 1) for dc in (0, 1)):
                for dr, dc, color in ((-1, -1, 1), (-1, 2, 2), (2, -1, 3), (2, 2, 4)):
                    target_row, target_col = row + dr, col + dc
                    if 0 <= target_row < height and 0 <= target_col < width:
                        output[target_row][target_col] = color
    return output
