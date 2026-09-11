def _objects(grid, gray):
    unseen = {
        (row, col) for row, line in enumerate(grid) for col, value in enumerate(line) if value
    }
    result = []
    while unseen:
        start = unseen.pop()
        component = {start}
        queue = [start]
        for row, col in queue:
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    neighbor = row + dr, col + dc
                    if (dr or dc) and neighbor in unseen:
                        unseen.remove(neighbor)
                        component.add(neighbor)
                        queue.append(neighbor)
        if not component & gray:
            result.append(component)
    return result


def solve(grid):
    gray = {
        (row, col) for row, line in enumerate(grid) for col, value in enumerate(line) if value == 5
    }
    top, bottom = min(r for r, _ in gray), max(r for r, _ in gray)
    left, right = min(c for _, c in gray), max(c for _, c in gray)
    colors = [
        value
        for row, line in enumerate(grid)
        for col, value in enumerate(line)
        if top <= row <= bottom and left <= col <= right and value not in (0, 5)
    ]
    objects = sorted(
        _objects(grid, gray),
        key=lambda cells: (min(r for r, _ in cells), min(c for _, c in cells)),
    )
    if len(objects) != len(colors):
        raise ValueError("task assumptions are not satisfied")
    output = [row[:] for row in grid]
    for cells, color in zip(objects, colors):
        for row, col in cells:
            output[row][col] = color
    return output
