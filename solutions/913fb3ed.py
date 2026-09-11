def solve(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    expansion_colors = {2: 1, 3: 6, 8: 4}
    for row in range(height):
        for col in range(width):
            if grid[row][col] != 0:
                continue
            colors = {
                expansion_colors[grid[row + dr][col + dc]]
                for dr in (-1, 0, 1)
                for dc in (-1, 0, 1)
                if (dr or dc)
                and 0 <= row + dr < height
                and 0 <= col + dc < width
                and grid[row + dr][col + dc] in expansion_colors
            }
            if len(colors) == 1:
                output[row][col] = colors.pop()
    return output
