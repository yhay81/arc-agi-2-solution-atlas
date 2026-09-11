def solve(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    for row in range(height):
        for col in range(width):
            if grid[row][col] == 3 and any(
                0 <= row + dr < height and 0 <= col + dc < width and grid[row + dr][col + dc] == 3
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1))
            ):
                output[row][col] = 8
    return output
