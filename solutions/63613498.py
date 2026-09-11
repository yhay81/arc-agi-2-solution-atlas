def solve(grid):
    h, w = len(grid), len(grid[0])
    divider = None
    for row in range(1, h):
        for col in range(1, w):
            color = grid[row][col]
            if color == 0:
                continue
            if all(value == color for value in grid[row][: col + 1]) and all(
                grid[r][col] == color for r in range(row + 1)
            ):
                candidate = (row, col, color)
                if divider is None or row + col > divider[0] + divider[1]:
                    divider = candidate
    if divider is None:
        return [row[:] for row in grid]
    split_row, split_col, divider_color = divider
    reference_cells = {
        (r, c) for r in range(split_row) for c in range(split_col) if grid[r][c] != 0
    }
    if not reference_cells:
        return [row[:] for row in grid]
    reference_values = {grid[row][col] for row, col in reference_cells}
    if len(reference_values) != 1:
        return [row[:] for row in grid]

    def signature(cells):
        top = min((row for row, _ in cells))
        left = min((col for _, col in cells))
        return frozenset(((row - top, col - left) for row, col in cells))

    reference_signature = signature(reference_cells)
    output = [row[:] for row in grid]
    excluded = {(row, col) for row in range(split_row + 1) for col in range(split_col + 1)}
    for color in sorted({value for row in grid for value in row}):
        if color in (0, divider_color):
            continue
        remaining = {
            (int(row), int(col))
            for row in range(h)
            for col in range(w)
            if grid[row][col] == color
            if (int(row), int(col)) not in excluded
        }
        while remaining:
            seed = remaining.pop()
            component = {seed}
            frontier = [seed]
            while frontier:
                row, col = frontier.pop()
                for neighbor in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                    if neighbor in remaining:
                        remaining.remove(neighbor)
                        component.add(neighbor)
                        frontier.append(neighbor)
            if signature(component) == reference_signature:
                for row, col in component:
                    output[row][col] = divider_color
    return output
