def solve(grid):
    h, w = len(grid), len(grid[0])
    remaining = {(r, c) for r in range(h) for c in range(w) if grid[r][c] == 3}
    if not remaining:
        return [row[:] for row in grid]
    clusters = []
    while remaining:
        seed = remaining.pop()
        cluster = {seed}
        frontier = [seed]
        while frontier:
            row, col = frontier.pop()
            for row_delta in (-1, 0, 1):
                for col_delta in (-1, 0, 1):
                    neighbor = (row + row_delta, col + col_delta)
                    if neighbor in remaining:
                        remaining.remove(neighbor)
                        cluster.add(neighbor)
                        frontier.append(neighbor)
        clusters.append(cluster)
    output = [row[:] for row in grid]
    for cluster in clusters:
        rows = [row for row, _ in cluster]
        cols = [col for _, col in cluster]
        top, bottom, left, right = (min(rows), max(rows), min(cols), max(cols))
        height, width = (bottom - top + 1, right - left + 1)
        if height != width or height % 2:
            return [row[:] for row in grid]
        size = height // 2
        quadrants = (
            (top, top + size, left, left + size),
            (top, top + size, left + size, right + 1),
            (top + size, bottom + 1, left, left + size),
            (top + size, bottom + 1, left + size, right + 1),
        )
        full = [
            all(grid[r][c] == 3 for r in range(a, b) for c in range(x, y))
            for a, b, x, y in quadrants
        ]
        empty = [
            all(grid[r][c] == 0 for r in range(a, b) for c in range(x, y))
            for a, b, x, y in quadrants
        ]
        if not (
            (full[0] and full[3] and empty[1] and empty[2])
            or (full[1] and full[2] and empty[0] and empty[3])
        ):
            return [row[:] for row in grid]
        for index in (position for position, is_full in enumerate(full) if not is_full):
            start_row = top - size if index < 2 else bottom + 1
            start_col = left - size if index % 2 == 0 else right + 1
            for row in range(start_row, start_row + size):
                for col in range(start_col, start_col + size):
                    if 0 <= row < h and 0 <= col < w and output[row][col] == 0:
                        output[row][col] = 8
    return output
