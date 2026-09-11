def solve(grid):
    from collections import Counter

    background = Counter(value for row in grid for value in row).most_common(1)[0][0]
    points = [
        (r, c, value)
        for r, row in enumerate(grid)
        for c, value in enumerate(row)
        if value != background
    ]
    r, c, color = min(points)
    output = [[background] * len(grid[0]) for _ in grid]
    for k in range(1, len(points) + 2):
        if 0 <= r - k < len(grid) and 0 <= c + k < len(grid[0]):
            output[r - k][c + k] = color
    return output
