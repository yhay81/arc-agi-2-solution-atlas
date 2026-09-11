def solve(grid):
    height, width = len(grid), len(grid[0])
    seeds = sorted((r, c) for r in range(height) for c in range(width) if grid[r][c] == 8)
    if len(seeds) < 2:
        return [row[:] for row in grid]
    slope = seeds[1][1] - seeds[0][1]
    if abs(slope) != 1 or any(
        seeds[index + 1] != (seeds[index][0] + 1, seeds[index][1] + slope)
        for index in range(len(seeds) - 1)
    ):
        return [row[:] for row in grid]
    hits = []
    for start, direction in ((seeds[0], (-1, -slope)), (seeds[-1], (1, slope))):
        path: list[tuple[int, int]] = []
        row, col = start
        row_delta, col_delta = direction
        while True:
            row += row_delta
            col += col_delta
            if not (0 <= row < height and 0 <= col < width):
                break
            if grid[row][col] == 2:
                hits.append((path, direction))
                break
            if grid[row][col] != 0:
                break
            path.append((row, col))
    if len(hits) != 1 or not hits[0][0]:
        return [row[:] for row in grid]
    path, (row_delta, col_delta) = hits[0]
    barrier = [(r, c) for r in range(height) for c in range(width) if grid[r][c] == 2]
    top, left = min(r for r, _ in barrier), min(c for _, c in barrier)
    bottom, right = max(r for r, _ in barrier), max(c for _, c in barrier)
    if bottom - top < right - left:
        row_delta = -row_delta
    else:
        col_delta = -col_delta
    output = [row[:] for row in grid]
    for row, col in path:
        output[row][col] = 3
    row, col = path[-1]
    while True:
        row += row_delta
        col += col_delta
        if not (0 <= row < height and 0 <= col < width):
            break
        if output[row][col] != 0:
            break
        output[row][col] = 3
    return output
