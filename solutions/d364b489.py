def solve(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    color_by_seed_offset = {(-1, 0): 8, (1, 0): 2, (0, -1): 6, (0, 1): 7}
    for row in range(height):
        for col in range(width):
            if grid[row][col] != 0:
                continue
            seeds = [
                offset
                for offset in color_by_seed_offset
                if 0 <= row + offset[0] < height
                and 0 <= col + offset[1] < width
                and grid[row + offset[0]][col + offset[1]] == 1
            ]
            if len(seeds) == 1:
                output[row][col] = color_by_seed_offset[seeds[0]]
    return output
