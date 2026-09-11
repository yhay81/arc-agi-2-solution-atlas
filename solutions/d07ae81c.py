def solve(grid):
    height, width = len(grid), len(grid[0])
    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    if len(counts) < 3:
        return [row[:] for row in grid]
    values = sorted(counts)
    base = set(sorted(values, key=lambda value: -counts[value])[:2])
    markers = [
        (r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value not in base
    ]
    if not markers:
        return [row[:] for row in grid]
    marker_to_base = {}
    for row, col in markers:
        marker = grid[row][col]
        neighbors = [
            grid[r][c]
            for r, c in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1))
            if 0 <= r < height and 0 <= c < width and grid[r][c] in base
        ]
        if not neighbors:
            return [row[:] for row in grid]
        candidate = max(base, key=lambda value: neighbors.count(value))
        if marker in marker_to_base and marker_to_base[marker] != candidate:
            return [row[:] for row in grid]
        marker_to_base[grid[row][col]] = candidate
    base_to_marker = {}
    for marker, color in marker_to_base.items():
        if color in base_to_marker and base_to_marker[color] != marker:
            return [row[:] for row in grid]
        base_to_marker[color] = marker
    if set(base_to_marker) != base:
        return [row[:] for row in grid]
    output = [row[:] for row in grid]
    for row, col in markers:
        for dr, dc in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
            r, c = row + dr, col + dc
            while 0 <= r < height and 0 <= c < width:
                if grid[r][c] in base_to_marker:
                    output[r][c] = base_to_marker[grid[r][c]]
                r, c = r + dr, c + dc
    return output
