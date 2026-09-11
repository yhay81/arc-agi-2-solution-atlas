def solve(grid):
    height, width = len(grid), len(grid[0])
    colors = {value for row in grid for value in row if value}
    if height != 3 or len(colors) != 1:
        return [row[:] for row in grid]
    remaining = {(r, c) for r in range(height) for c in range(width) if not grid[r][c]}
    regions = []
    while remaining:
        start = remaining.pop()
        stack, cells = [start], [start]
        while stack:
            r, c = stack.pop()
            for point in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if point in remaining:
                    remaining.remove(point)
                    cells.append(point)
                    stack.append(point)
        regions.append(cells)
    if len(regions) < 4 or any(len(region) not in (1, 3, 4) for region in regions):
        return [row[:] for row in grid]
    regions.sort(key=lambda region: sum(c for _, c in region) / len(region))
    output = [row[:] for row in grid]
    for index, region in enumerate(regions):
        if index % 3 == 0:
            for row, col in region:
                output[row][col] = 4
    return output
