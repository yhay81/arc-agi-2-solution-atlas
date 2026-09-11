from itertools import pairwise, permutations


def line(first, second):
    row, col = first
    end_row, end_col = second
    delta_row, delta_col = end_row - row, end_col - col
    if delta_row and delta_col and abs(delta_row) != abs(delta_col):
        return []
    step_row = 0 if not delta_row else (1 if delta_row > 0 else -1)
    step_col = 0 if not delta_col else (1 if delta_col > 0 else -1)
    length = max(abs(delta_row), abs(delta_col))
    return [(row + i * step_row, col + i * step_col) for i in range(length + 1)]


def distance(first, second):
    return max(abs(first[0] - second[0]), abs(first[1] - second[1]))


def solve(grid):
    source = [list(row) for row in grid]
    height, width = len(source), len(source[0])
    output = [row[:] for row in source]
    rendered = {}
    colors = sorted({value for row in source for value in row if value})
    for color in colors:
        points = [
            (r, c) for r, row in enumerate(source) for c, value in enumerate(row) if value == color
        ]
        if len(points) < 2 or len(points) > 8:
            continue

        cycle = None
        if len(points) >= 3:
            first = points[0]
            for rest in permutations(points[1:]):
                if rest[0] > rest[-1]:
                    continue
                order = (first, *rest)
                edges = tuple(zip(order, (*order[1:], first), strict=True))
                if not all(line(a, b) for a, b in edges):
                    continue
                candidate = (sum(distance(a, b) for a, b in edges), order)
                if cycle is None or candidate < cycle:
                    cycle = candidate
        if cycle is not None:
            order = cycle[1]
            edges = zip(order, (*order[1:], order[0]), strict=True)
        else:
            path = None
            for order in permutations(points):
                edges = tuple(pairwise(order))
                if not all(line(a, b) for a, b in edges):
                    continue
                candidate = (sum(distance(a, b) for a, b in edges), order)
                if path is None or candidate < path:
                    path = candidate
            edges = pairwise(path[1]) if path is not None else ()

        cells = set(points)
        for first, second in edges:
            cells.update(line(first, second))
        rendered[color] = cells
        for row, col in cells:
            if output[row][col] == 0:
                output[row][col] = color

    for color in colors:
        points = [
            (r, c) for r, row in enumerate(source) for c, value in enumerate(row) if value == color
        ]
        if len(points) != 1 or not rendered:
            continue
        anchor = points[0]
        choices = []
        for other, cells in rendered.items():
            other_points = [
                (r, c)
                for r, row in enumerate(source)
                for c, value in enumerate(row)
                if value == other
            ]
            nearest = min(
                other_points,
                key=lambda point: abs(point[0] - anchor[0]) + abs(point[1] - anchor[1]),
            )
            choices.append(
                (abs(nearest[0] - anchor[0]) + abs(nearest[1] - anchor[1]), other, nearest)
            )
        _, other, nearest = min(choices)
        row_shift, col_shift = anchor[0] - nearest[0], anchor[1] - nearest[1]
        for row, col in rendered[other]:
            target_row, target_col = row + row_shift, col + col_shift
            if (
                0 <= target_row < height
                and 0 <= target_col < width
                and output[target_row][target_col] == 0
            ):
                output[target_row][target_col] = color
    return output
