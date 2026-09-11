import itertools


def _transform(grid, transform):
    output = [list(row) for row in grid]
    if transform >= 4:
        output = [row[::-1] for row in output]
    for _ in range(transform % 4):
        output = [list(row) for row in zip(*output[::-1])]
    return output


def _components(grid):
    unseen = {(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value}
    result = []
    while unseen:
        start = min(unseen)
        unseen.remove(start)
        queue = [start]
        component = []
        for row, col in queue:
            component.append((row, col))
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                neighbor = row + dr, col + dc
                if neighbor in unseen and grid[neighbor[0]][neighbor[1]] == grid[row][col]:
                    unseen.remove(neighbor)
                    queue.append(neighbor)
        result.append(component)
    return result


def _bbox(cells):
    rows, cols = zip(*cells)
    return min(rows), max(rows), min(cols), max(cols)


def _normalized_shape(cells):
    top, bottom, left, right = _bbox(cells)
    points = set(cells)
    return [
        [int((row, col) in points) for col in range(left, right + 1)]
        for row in range(top, bottom + 1)
    ]


def _compress(grid):
    rows = [list(row) for row, _ in itertools.groupby(map(tuple, grid))]
    columns = [column for column, _ in itertools.groupby(zip(*rows))]
    return [list(row) for row in zip(*columns)]


def _shape_key(cells):
    shape = _compress(_normalized_shape(cells))
    return min(tuple(map(tuple, _transform(shape, transform))) for transform in range(8))


def solve(grid):
    components = _components(grid)
    reference = min(components, key=min)
    key = _shape_key(reference)
    output = [row[:] for row in grid]
    for component in components:
        if _shape_key(component) == key:
            for row, col in component:
                output[row][col] = 2
    return output
