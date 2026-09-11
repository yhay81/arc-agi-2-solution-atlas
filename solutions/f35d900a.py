from collections import Counter


def solve(grid):
    if not grid or not grid[0]:
        return [row[:] for row in grid]
    h, w = len(grid), len(grid[0])
    positions = [(r, c) for r in range(h) for c in range(w) if grid[r][c] != 0]
    if len(positions) != 4:
        return [row[:] for row in grid]
    counts = Counter(grid[r][c] for r, c in positions)
    colors = sorted(counts)
    if len(colors) != 2 or set(counts.values()) != {2}:
        return [row[:] for row in grid]
    rows = sorted({row for row, _ in positions})
    cols = sorted({col for _, col in positions})
    if len(rows) != 2 or len(cols) != 2:
        return [row[:] for row in grid]
    marker_by_position = {(row, col): grid[row][col] for row, col in positions}
    corners = [(row, col) for row in rows for col in cols]
    if any(position not in marker_by_position for position in corners):
        return [row[:] for row in grid]
    if any((row <= 0 or row >= h - 1 or col <= 0 or col >= w - 1 for row, col in corners)):
        return [row[:] for row in grid]
    output = [[0] * w for _ in range(h)]
    other_color = {value: colors[1] if value == colors[0] else colors[0] for value in colors}
    for row, col in corners:
        center_color = marker_by_position[row, col]
        ring_color = other_color[center_color]
        output[row][col] = center_color
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr or dc:
                    output[row + dr][col + dc] = ring_color
    for row in rows:
        left, right = cols
        half_distance = (right - left) // 2
        for distance in range(2, half_distance + 1, 2):
            output[row][left + distance] = 5
            output[row][right - distance] = 5
    for col in cols:
        top, bottom = rows
        half_distance = (bottom - top) // 2
        for distance in range(2, half_distance + 1, 2):
            output[top + distance][col] = 5
            output[bottom - distance][col] = 5
    return output
