def _components(grid, diagonal):
    remaining = {
        (row, col) for row, values in enumerate(grid) for col, value in enumerate(values) if value
    }
    directions = [
        (dr, dc)
        for dr in (-1, 0, 1)
        for dc in (-1, 0, 1)
        if (dr or dc) and (diagonal or not (dr and dc))
    ]
    found = []
    while remaining:
        start = min(remaining)
        remaining.remove(start)
        stack = [start]
        cells = []
        while stack:
            row, col = stack.pop()
            cells.append((row, col))
            for dr, dc in directions:
                point = row + dr, col + dc
                if point in remaining:
                    remaining.remove(point)
                    stack.append(point)
        found.append(cells)
    return found


def _find_frame(grid):
    height, width = len(grid), len(grid[0])
    for color in sorted({value for row in grid for value in row if value}):
        cells = {
            (row, col) for row in range(height) for col in range(width) if grid[row][col] == color
        }
        rows = sorted({row for row, _ in cells})
        cols = sorted({col for _, col in cells})
        if (
            len(cells) == 4
            and len(rows) == len(cols) == 2
            and cells == {(r, c) for r in rows for c in cols}
        ):
            return color, rows, cols
    return None


def _crop(grid, cells):
    top = min(row for row, _ in cells)
    bottom = max(row for row, _ in cells)
    left = min(col for _, col in cells)
    right = max(col for _, col in cells)
    return [row[left : right + 1] for row in grid[top : bottom + 1]]


def _solid_square_sizes(grid, excluded):
    sizes = []
    for color in sorted({value for row in grid for value in row} - excluded):
        mask = [[value == color for value in row] for row in grid]
        for cells in _components(mask, False):
            rows = [row for row, _ in cells]
            cols = [col for _, col in cells]
            size = max(rows) - min(rows) + 1
            if size == max(cols) - min(cols) + 1 and len(cells) == size * size:
                sizes.append(size)
    return sizes


def _scale(grid, factor):
    return [[value for value in row for _ in range(factor)] for row in grid for _ in range(factor)]


def solve(grid):
    frame = _find_frame(grid)
    if frame is None:
        return [row[:] for row in grid]
    frame_color, (top, bottom), (left, right) = frame
    output = [row[left : right + 1] for row in grid[top : bottom + 1]]
    outside = [row[:] for row in grid]
    for row in range(top, bottom + 1):
        outside[row][left : right + 1] = [0] * (right - left + 1)
    keys = _components(outside, True)
    if len(keys) != 1:
        return [row[:] for row in grid]
    key = _crop(outside, keys[0])
    scales = _solid_square_sizes(output, {0, frame_color})
    if not scales:
        return [row[:] for row in grid]
    expanded = _scale(key, max(scales))
    height, width = len(expanded), len(expanded[0])
    if height > len(output) or width > len(output[0]):
        return [row[:] for row in grid]

    existing = {
        (row, col)
        for row, values in enumerate(output)
        for col, value in enumerate(values)
        if value not in (0, frame_color)
    }
    matches = [
        (row, col)
        for row in range(len(output) - height + 1)
        for col in range(len(output[0]) - width + 1)
        if all(
            row <= r < row + height
            and col <= c < col + width
            and expanded[r - row][c - col] == output[r][c]
            for r, c in existing
        )
    ]
    if len(matches) != 1:
        return [row[:] for row in grid]
    top, left = matches[0]
    for row, values in enumerate(expanded):
        for col, value in enumerate(values):
            if value:
                output[top + row][left + col] = value
    return output
