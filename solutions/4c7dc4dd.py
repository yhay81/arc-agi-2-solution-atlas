def _find_blocks(grid):
    height, width = len(grid), len(grid[0])
    groups = {}
    for size in range(5, 10):
        for top in range(height - size + 1):
            for left in range(width - size + 1):
                color = grid[top][left]
                border = [grid[top][left + offset] for offset in range(size)] + [
                    grid[top + size - 1][left + offset] for offset in range(size)
                ]
                border += [grid[top + offset][left] for offset in range(size)]
                border += [grid[top + offset][left + size - 1] for offset in range(size)]
                if not color or any(value != color for value in border):
                    continue
                block = [row[left + 1 : left + size - 1] for row in grid[top + 1 : top + size - 1]]
                colors = {value for row in block for value in row if value}
                if sum(value == 0 for row in block for value in row) >= 4 and len(colors) <= 2:
                    groups.setdefault(size, []).append(block)
    return next(blocks for blocks in groups.values() if len(blocks) == 4)


def _distances(height, width, mode):
    if mode == "center":
        center = height // 2, width // 2
        return [
            [abs(row - center[0]) + abs(col - center[1]) for col in range(width)]
            for row in range(height)
        ]
    return [
        [min(row, height - 1 - row) + min(col, width - 1 - col) for col in range(width)]
        for row in range(height)
    ]


def _transform(block, operation, parameter=None):
    height, width = len(block), len(block[0])
    colors = {value for row in block for value in row if value}
    if operation == "complement":
        if len(colors) != 1:
            return None
        color = next(iter(colors))
        return [[color if value == 0 else 0 for value in row] for row in block]
    if operation == "connect":
        fill = next((color for color in colors if color != parameter), None)
        if fill is None:
            return None
        output = [row[:] for row in block]
        for row in range(height):
            points = [col for col, value in enumerate(block[row]) if value]
            for left, right in zip(points, points[1:]):
                output[row][left + 1 : right] = [fill] * (right - left - 1)
        for col in range(width):
            points = [row for row in range(height) if block[row][col]]
            for top, bottom in zip(points, points[1:]):
                for row in range(top + 1, bottom):
                    output[row][col] = fill
        return output
    if operation == "ripple":
        if height % 2 == 0 or width % 2 == 0:
            return None
        distances = _distances(height, width, "center")
        profile = []
        for distance in range(max(map(max, distances)) + 1):
            values = {
                block[row][col]
                for row in range(height)
                for col in range(width)
                if distances[row][col] == distance
            }
            if len(values) != 1:
                return None
            profile.append(next(iter(values)))
        try:
            start = profile.index(0)
        except ValueError:
            return None
        if not start or any(profile[start:]):
            return None
        return [
            [0 if distance < start else profile[(distance - start) % start] for distance in row]
            for row in distances
        ]

    distances = _distances(height, width, "corners")
    rings = {0: 0}
    for row in range(height):
        for col in range(width):
            if block[row][col]:
                distance = distances[row][col]
                if distance in rings and rings[distance] != block[row][col]:
                    return None
                rings[distance] = block[row][col]
    if len(rings) != max(rings) + 1:
        return None
    maximum = max(rings)
    return [[rings[min(distance, maximum)] for distance in row] for row in distances]


def solve(grid):
    blocks = _find_blocks(grid)
    examples = [block for block in blocks if any(value for row in block for value in row)]
    candidates = []
    for source_index, source in enumerate(examples):
        colors = {value for row in source for value in row if value}
        for target_index, target in enumerate(examples):
            if source_index == target_index or colors != {
                value for row in target for value in row if value
            }:
                continue
            query = examples[3 - source_index - target_index]
            operations = [(name, None) for name in ("complement", "ripple", "corner_rings")]
            operations += [("connect", color) for color in colors]
            for operation, parameter in operations:
                prediction = _transform(source, operation, parameter)
                answer = _transform(query, operation, parameter)
                if prediction == target and answer is not None:
                    score = abs(
                        sum(value != 0 for row in source for value in row)
                        - sum(value != 0 for row in query for value in row)
                    )
                    candidates.append((score, answer))
    best = min(score for score, _ in candidates)
    unique = {tuple(map(tuple, prediction)) for score, prediction in candidates if score == best}
    if len(unique) != 1:
        raise ValueError("task assumptions are not satisfied")
    return [list(row) for row in unique.pop()]
