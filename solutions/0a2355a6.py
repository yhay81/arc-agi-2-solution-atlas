def _components(cells):
    unseen = set(cells)
    result = []
    while unseen:
        start = unseen.pop()
        component = {start}
        queue = [start]
        for row, col in queue:
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                neighbor = row + dr, col + dc
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    component.add(neighbor)
                    queue.append(neighbor)
        result.append(component)
    return result


def solve(grid):
    output = [row[:] for row in grid]
    colors = {value for row in grid for value in row} - {0}
    for color in colors:
        cells = {
            (row, col)
            for row, line in enumerate(grid)
            for col, value in enumerate(line)
            if value == color
        }
        for shape in _components(cells):
            top = min(row for row, _ in shape) - 1
            bottom = max(row for row, _ in shape) + 1
            left = min(col for _, col in shape) - 1
            right = max(col for _, col in shape) + 1
            empty = {
                (row, col)
                for row in range(top, bottom + 1)
                for col in range(left, right + 1)
                if (row, col) not in shape
            }
            holes = sum(
                not any(row in (top, bottom) or col in (left, right) for row, col in component)
                for component in _components(empty)
            )
            replacement = {1: 1, 2: 3, 3: 2, 4: 4}.get(holes, color)
            for row, col in shape:
                output[row][col] = replacement
    return output
