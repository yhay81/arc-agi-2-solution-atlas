from collections import Counter


def _components(grid, color):
    height, width = len(grid), len(grid[0])
    remaining = {
        (row, col) for row in range(height) for col in range(width) if grid[row][col] == color
    }
    groups = []
    while remaining:
        start = min(remaining)
        remaining.remove(start)
        stack = [start]
        cells = []
        while stack:
            row, col = stack.pop()
            cells.append((row, col))
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    point = row + dr, col + dc
                    if (dr or dc) and point in remaining:
                        remaining.remove(point)
                        stack.append(point)
        groups.append(sorted(cells))
    return groups


def _sign(value, fallback):
    value = value if abs(value) > 1e-9 else fallback
    return 1 if value > 0 else -1 if value < 0 else 0


def _distance(point, cells):
    return min(max(abs(row - point[0]), abs(col - point[1])) for row, col in cells)


def _route(start, end, wire, marker):
    rows = [row for row, _ in marker]
    cols = [col for _, col in marker]
    top, bottom, left, right = min(rows), max(rows), min(cols), max(cols)
    centroid = sum(rows) / len(marker), sum(cols) / len(marker)
    mass = (
        sum(row for row, _ in wire) / len(wire) - end[0],
        sum(col for _, col in wire) / len(wire) - end[1],
    )
    dr = _sign(centroid[0] - end[0], mass[0])
    dc = _sign(centroid[1] - end[1], mass[1])
    if not (dr and dc):
        raise ValueError("task assumptions are not satisfied")

    path = [start]
    while _distance(path[-1], marker) > 1:
        row, col = path[-1]
        next_row = min(row + dr, bottom + 1) if dr > 0 else max(row + dr, top - 1)
        next_col = min(col + dc, right + 1) if dc > 0 else max(col + dc, left - 1)
        if (next_row, next_col) == path[-1]:
            raise ValueError("task assumptions are not satisfied")
        path.append((next_row, next_col))

    row, col = path[-1]
    row_contact = any(r == row + dr and abs(c - col) <= 1 for r, c in marker)
    if row_contact:
        values = range(top, bottom + 1) if dr > 0 else range(bottom, top - 1, -1)
        for row in values:
            columns = [col for marker_row, col in marker if marker_row == row]
            point = row, max(columns) + 1 if dc > 0 else min(columns) - 1
            if path[-1] != point:
                path.append(point)
        exit_direction = dr, -dc
    else:
        values = range(left, right + 1) if dc > 0 else range(right, left - 1, -1)
        for col in values:
            rows = [row for row, marker_col in marker if marker_col == col]
            point = max(rows) + 1 if dr > 0 else min(rows) - 1, col
            if path[-1] != point:
                path.append(point)
        exit_direction = -dr, dc
    while len(path) < len(wire):
        path.append((path[-1][0] + exit_direction[0], path[-1][1] + exit_direction[1]))
    return path[: len(wire)]


def solve(grid):
    height, width = len(grid), len(grid[0])
    background = Counter(value for row in grid for value in row).most_common(1)[0][0]
    colors = {value for row in grid for value in row} - {background}
    groups = {
        (color, index): cells
        for color in colors
        for index, cells in enumerate(_components(grid, color))
    }
    lines = {
        key: cells
        for key, cells in groups.items()
        if len(cells) >= 3
        and (len({row for row, _ in cells}) == 1 or len({col for _, col in cells}) == 1)
    }

    systems = []
    used = set()
    for line, cells in lines.items():
        matches = []
        for wire, wire_cells in groups.items():
            if wire == line or wire in lines:
                continue
            for end in (cells[0], cells[-1]):
                attached = [
                    point
                    for point in wire_cells
                    if abs(point[0] - end[0]) + abs(point[1] - end[1]) == 1
                ]
                if len(attached) == 1:
                    matches.append((wire, end, attached[0]))
        if len(matches) == 1:
            wire, end, start = matches[0]
            systems.append((line, wire, end, start))
            used |= {line, wire}

    markers = {key: cells for key, cells in groups.items() if key not in used}
    if len(markers) != len(systems):
        raise ValueError("task assumptions are not satisfied")
    output = [row[:] for row in grid]
    for _, wire, end, start in systems:
        wire_cells = groups[wire]
        marker = min(markers, key=lambda key: _distance(end, markers[key]))
        marker_cells = markers.pop(marker)
        for row, col in wire_cells:
            output[row][col] = background
        for row, col in _route(start, end, wire_cells, marker_cells):
            if 0 <= row < height and 0 <= col < width:
                output[row][col] = wire[0]
    return output
