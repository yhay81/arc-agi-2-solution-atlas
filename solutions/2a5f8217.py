def _components(grid):
    unseen = {(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value}
    result = []
    while unseen:
        start = min(unseen)
        unseen.remove(start)
        cells = {start}
        queue = [start]
        for row, col in queue:
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                neighbor = row + dr, col + dc
                if neighbor in unseen and grid[neighbor[0]][neighbor[1]] == grid[row][col]:
                    unseen.remove(neighbor)
                    cells.add(neighbor)
                    queue.append(neighbor)
        result.append(cells)
    return result


def _shape(cells):
    top = min(row for row, _ in cells)
    left = min(col for _, col in cells)
    return {(row - top, col - left) for row, col in cells}


def solve(grid):
    components = _components(grid)
    output = [row[:] for row in grid]
    for cells in components:
        row, col = next(iter(cells))
        if grid[row][col] != 1:
            continue
        matches = [
            other
            for other in components
            if other != cells
            and _shape(other) == _shape(cells)
            and grid[next(iter(other))[0]][next(iter(other))[1]] != 1
        ]
        if len(matches) == 1:
            match_row, match_col = next(iter(matches[0]))
            color = grid[match_row][match_col]
            for cell_row, cell_col in cells:
                output[cell_row][cell_col] = color
    return output
