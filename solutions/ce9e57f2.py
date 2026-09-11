def solve(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    remaining = {(r, c) for r in range(height) for c in range(width) if grid[r][c] == 2}
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
        rows, cols = sorted(r for r, _ in cells), [c for _, c in cells]
        if len(set(cols)) != 1 or rows != list(range(min(rows), max(rows) + 1)):
            return [row[:] for row in grid]
        start_row = min(rows) + (len(rows) + 1) // 2
        for row in rows:
            if row >= start_row:
                output[row][cols[0]] = 8
    return output
