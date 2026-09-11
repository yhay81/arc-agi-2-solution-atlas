from collections import Counter, defaultdict


def _components(grid, colors):
    height, width = len(grid), len(grid[0])
    remaining = {
        (row, col) for row in range(height) for col in range(width) if grid[row][col] in colors
    }
    found = []
    while remaining:
        start = min(remaining)
        color = grid[start[0]][start[1]]
        remaining.remove(start)
        stack = [start]
        cells = []
        while stack:
            row, col = stack.pop()
            cells.append((row, col))
            for point in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                if point in remaining and grid[point[0]][point[1]] == color:
                    remaining.remove(point)
                    stack.append(point)
        found.append((color, cells))
    return found


def _signature(cells):
    top = min(row for row, _ in cells)
    left = min(col for _, col in cells)
    bottom = max(row for row, _ in cells)
    right = max(col for _, col in cells)
    points = {(row - top, col - left) for row, col in cells}
    return tuple(
        tuple((row, col) in points for col in range(right - left + 1))
        for row in range(bottom - top + 1)
    )


def _boundary_colors(grid, cells, background):
    colors = []
    for row, col in cells:
        for next_row, next_col in (
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 1),
        ):
            if grid[next_row][next_col] != background:
                colors.append(grid[next_row][next_col])
    return colors


def solve(grid):
    height, width = len(grid), len(grid[0])
    counts = Counter(value for row in grid for value in row)
    background = min(counts, key=lambda color: (-counts[color], color))
    by_shape = defaultdict(list)
    for color, cells in _components(grid, set(range(10)) - {background}):
        by_shape[_signature(cells)].append((color, cells))

    holes = [
        cells
        for _, cells in _components(grid, {background})
        if all(0 < row < height - 1 and 0 < col < width - 1 for row, col in cells)
    ]
    boundaries = [color for hole in holes for color in _boundary_colors(grid, hole, background)]
    if not boundaries:
        return [row[:] for row in grid]
    boundary_color = Counter(boundaries).most_common(1)[0][0]

    output = [row[:] for row in grid]
    removed = []
    for hole in holes:
        colors = _boundary_colors(grid, hole, background)
        if not colors or Counter(colors).most_common(1)[0][0] != boundary_color:
            continue
        matches = by_shape.get(_signature(hole), [])
        if not matches:
            continue
        color, component = max(
            matches,
            key=lambda item: (
                len(item[1]),
                not any(row in (0, height - 1) or col in (0, width - 1) for row, col in item[1]),
            ),
        )
        removed.append(component)
        for row, col in hole:
            output[row][col] = color
    for component in removed:
        for row, col in component:
            output[row][col] = background
    return output
