def solve(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    colors_by_degree = {2: 1, 3: 4, 4: 2}
    for row in range(height):
        for col in range(width):
            if grid[row][col] != 5:
                continue
            degree = sum(
                0 <= row + dr < height and 0 <= col + dc < width and grid[row + dr][col + dc] == 5
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1))
            )
            output[row][col] = colors_by_degree.get(degree, 5)
    return output
