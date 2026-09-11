def _fill_enclosed_with_four(grid):
    output = [row[:] for row in grid]
    height, width = len(grid), len(grid[0])
    seen = [[False] * width for _ in range(height)]
    stack = [
        (row, col)
        for row in range(height)
        for col in range(width)
        if (row in (0, height - 1) or col in (0, width - 1)) and grid[row][col] == 0
    ]
    while stack:
        row, col = stack.pop()
        if not (0 <= row < height and 0 <= col < width) or seen[row][col] or grid[row][col] != 0:
            continue
        seen[row][col] = True
        stack.extend(((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)))
    for row in range(height):
        for col in range(width):
            if grid[row][col] == 0 and not seen[row][col]:
                output[row][col] = 4
    return output


def solve(grid):
    return _fill_enclosed_with_four(grid)
