from collections import Counter


def _candidate_rectangles(top, bottom, left, right):
    yield top, bottom, left, right, 0, 0, 0
    for length in range(1, bottom - top + 1):
        yield top + length, bottom, left, right, -length, 0, 1
        yield top, bottom - length, left, right, length, 0, 2
    for length in range(1, right - left + 1):
        yield top, bottom, left + length, right, 0, -length, 3
        yield top, bottom, left, right - length, 0, length, 4


def _stick_length(outside, direction, bounds):
    if direction == 0:
        return 0 if not outside else None
    if not outside:
        return None
    top, bottom, left, right = bounds
    rows = [row for row, _ in outside]
    cols = [col for _, col in outside]
    if direction in (1, 2):
        if len(set(cols)) != 1 or len(outside) != max(rows) - min(rows) + 1:
            return None
        if (direction == 1 and min(rows) != top) or (direction == 2 and max(rows) != bottom):
            return None
    else:
        if len(set(rows)) != 1 or len(outside) != max(cols) - min(cols) + 1:
            return None
        if (direction == 3 and min(cols) != left) or (direction == 4 and max(cols) != right):
            return None
    return len(outside)


def _infer_object(grid, color, background):
    positions = [
        (row, col)
        for row, values in enumerate(grid)
        for col, value in enumerate(values)
        if value == color
    ]
    rows, cols = [row for row, _ in positions], [col for _, col in positions]
    bounds = min(rows), max(rows), min(cols), max(cols)
    candidates = []
    for top, bottom, left, right, row_shift, col_shift, direction in _candidate_rectangles(*bounds):
        crop = [grid[row][left : right + 1] for row in range(top, bottom + 1)]
        if any(value == background for row in crop for value in row):
            continue
        outside = [
            point
            for point in positions
            if not (top <= point[0] <= bottom and left <= point[1] <= right)
        ]
        length = _stick_length(outside, direction, bounds)
        if length is None:
            continue
        expected = (
            top - bounds[0]
            if direction == 1
            else bounds[1] - bottom
            if direction == 2
            else left - bounds[2]
            if direction == 3
            else bounds[3] - right
            if direction == 4
            else 0
        )
        if length != expected:
            continue
        area = (bottom - top + 1) * (right - left + 1)
        visible = sum(value == color for row in crop for value in row)
        candidates.append(
            (
                visible / area,
                area,
                direction != 0,
                (color, top, bottom, left, right, row_shift, col_shift, length),
            )
        )
    if not candidates:
        return None
    chosen = max(candidates, key=lambda item: item[:3])[3]
    if chosen[-1] == 1:
        return color, *bounds, 0, 0
    return chosen[:-1]


def _depth_order(grid, objects, colors, background):
    above = {color: set() for color in colors}
    for row, values in enumerate(grid):
        for col, winner in enumerate(values):
            if winner == background:
                continue
            for color, top, bottom, left, right, _, _ in objects:
                if color != winner and top <= row <= bottom and left <= col <= right:
                    above[winner].add(color)
    remaining = set(colors)
    order = []
    while remaining:
        lower = sorted(color for color in remaining if not above[color] & remaining)
        if not lower:
            lower = [min(remaining)]
        order.extend(lower)
        remaining.difference_update(lower)
    return order


def solve(grid):
    height, width = len(grid), len(grid[0])
    counts = Counter(value for row in grid for value in row)
    background = max(counts, key=lambda value: (counts[value], -value))
    colors = sorted(value for value in counts if value != background)
    objects = [_infer_object(grid, color, background) for color in colors]
    if not colors or any(item is None for item in objects):
        return [row[:] for row in grid]

    output = [[background] * width for _ in range(height)]
    by_color = {item[0]: item for item in objects}
    for color in _depth_order(grid, objects, colors, background):
        _, top, bottom, left, right, row_shift, col_shift = by_color[color]
        for row in range(top, bottom + 1):
            for col in range(left, right + 1):
                target = row + row_shift, col + col_shift
                if 0 <= target[0] < height and 0 <= target[1] < width:
                    output[target[0]][target[1]] = color
    return output
