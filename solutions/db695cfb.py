from collections import Counter


def solve(grid):
    h, w = len(grid), len(grid[0])
    counts = Counter(value for row in grid for value in row)
    background = max(range(10), key=lambda value: counts[value])
    points_by_color = {
        color: [(r, c) for r in range(h) for c in range(w) if grid[r][c] == color]
        for color in counts
        if color != background
    }
    candidates = {}
    for color, points in points_by_color.items():
        for index, (r0, c0) in enumerate(points):
            for r1, c1 in points[index + 1 :]:
                dr, dc = r1 - r0, c1 - c0
                if dr == 0 or abs(dr) != abs(dc):
                    continue
                slope = 1 if dr * dc > 0 else -1
                key = c0 - r0 if slope == 1 else c0 + r0
                candidates.setdefault(color, []).append(
                    (abs(dr), slope, key, min(r0, r1), max(r0, r1))
                )
    if not candidates:
        return [row[:] for row in grid]
    reference_color = max(
        candidates,
        key=lambda color: (
            len(candidates[color]),
            sum(item[0] for item in candidates[color]),
            -color,
        ),
    )
    reference_lines = {
        (slope, key, top, bottom) for _, slope, key, top, bottom in candidates[reference_color]
    }
    output = [row[:] for row in grid]
    for slope, key, top, bottom in reference_lines:
        for row in range(top, bottom + 1):
            col = row + key if slope == 1 else key - row
            if 0 <= col < w:
                output[row][col] = reference_color
    for color, points in points_by_color.items():
        if color == reference_color:
            continue
        for row, col in points:
            matches = [
                (slope, key)
                for slope, key, top, bottom in reference_lines
                if top <= row <= bottom and (col - row if slope == 1 else col + row) == key
            ]
            if not matches:
                continue
            slope, key = matches[0]
            for target_row in range(h):
                target_col = row + col - target_row if slope == 1 else target_row + (col - row)
                if 0 <= target_col < w:
                    output[target_row][target_col] = color
    return output
