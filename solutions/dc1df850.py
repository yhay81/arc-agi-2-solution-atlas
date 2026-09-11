def solve(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    for row in range(height):
        for col in range(width):
            if grid[row][col] != 0:
                continue
            if any(
                0 <= row + dr < height and 0 <= col + dc < width and grid[row + dr][col + dc] == 2
                for dr in (-1, 0, 1)
                for dc in (-1, 0, 1)
                if dr or dc
            ):
                output[row][col] = 1
    return output
