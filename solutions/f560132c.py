import math


def _find_palette(grid):
    height, width = len(grid), len(grid[0])
    candidates = []
    for size in (2, 3):
        for top in range(height - size + 1):
            for left in range(width - size + 1):
                patch = [grid[row][left : left + size] for row in range(top, top + size)]
                if len({value for row in patch for value in row}) == size * size:
                    candidates.append(
                        (size, sum(value != 0 for row in patch for value in row), top, left)
                    )
    size, _, top, left = max(candidates)
    return [row[left : left + size] for row in grid[top : top + size]], top, left


def _components(mask):
    height, width = len(mask), len(mask[0])
    remaining = {(row, col) for row in range(height) for col in range(width) if mask[row][col]}
    parts = []
    while remaining:
        start = remaining.pop()
        stack = [start]
        cells = [start]
        while stack:
            row, col = stack.pop()
            for point in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                if point in remaining:
                    remaining.remove(point)
                    stack.append(point)
                    cells.append(point)
        parts.append(cells)
    return parts


def _shape(cells):
    top = min(row for row, _ in cells)
    left = min(col for _, col in cells)
    bottom = max(row for row, _ in cells)
    right = max(col for _, col in cells)
    shape = [[False] * (right - left + 1) for _ in range(bottom - top + 1)]
    for row, col in cells:
        shape[row - top][col - left] = True
    return shape


def _extract_shapes(grid, palette_top, palette_left, palette_size):
    mask = [[value != 0 for value in row] for row in grid]
    for row in range(palette_top, palette_top + palette_size):
        for col in range(palette_left, palette_left + palette_size):
            mask[row][col] = True
    parts = _components(mask)
    anchor = next(
        index for index, cells in enumerate(parts) if (palette_top, palette_left) in cells
    )
    parts.insert(0, parts.pop(anchor))
    return [_shape(cells) for cells in parts]


def _rotate(shape):
    return [list(row) for row in zip(*shape[::-1])]


def _orientations(shape, anchor):
    for turns in (0,) if anchor else (0, 3, 1, 2):
        result = shape
        for _ in range(turns):
            result = _rotate(result)
        yield result


def _valid_slots(cells, top, left, rows, cols, size):
    corner_points = ((0, 0), (0, size - 1), (size - 1, 0), (size - 1, size - 1))
    corner_hits = [point for point in corner_points if point in cells]
    hits = []
    for slot in range(rows * cols):
        slot_row, slot_col = divmod(slot, cols)
        corner = slot_row in (0, rows - 1) and slot_col in (0, cols - 1)
        corner_point = (
            0 if slot_row == 0 else size - 1,
            0 if slot_col == 0 else size - 1,
        )
        if corner:
            valid = corner_hits == [corner_point]
        else:
            shape_height = max(row for row, _ in cells) - top + 1
            shape_width = max(col for _, col in cells) - left + 1
            valid = (
                not corner_hits
                and (top == 0) == (slot_row == 0)
                and ((top + shape_height == size) == (slot_row == rows - 1))
                and (left == 0) == (slot_col == 0)
                and ((left + shape_width == size) == (slot_col == cols - 1))
            )
        if valid:
            hits.append(slot)
    return hits


def _placement_options(shapes, rows, cols, size):
    slots = range(rows * cols)
    options = {slot: [] for slot in slots}
    for shape_index, shape in enumerate(shapes):
        for rotated in _orientations(shape, shape_index == 0):
            shape_height, shape_width = len(rotated), len(rotated[0])
            points = [
                (row, col)
                for row in range(shape_height)
                for col in range(shape_width)
                if rotated[row][col]
            ]
            for top in range(size - shape_height + 1):
                for left in range(size - shape_width + 1):
                    cells = {(row + top, col + left) for row, col in points}
                    hits = _valid_slots(cells, top, left, rows, cols, size)
                    if len(hits) != 1 or (shape_index == 0) != (hits[0] == 0):
                        continue
                    bits = sum(1 << (row * size + col) for row, col in cells)
                    options[hits[0]].append((shape_index, bits, cells))
    areas = [sum(sum(row) for row in shape) for shape in shapes]
    for slot in slots:
        options[slot].sort(key=lambda item: areas[item[0]])
    return options


def _exact_cover(options, size):
    full = (1 << (size * size)) - 1
    failed = set()

    def search(remaining, used, occupied, chosen):
        state = tuple(remaining), used, occupied
        if state in failed:
            return None
        if not remaining:
            return chosen
        choices = []
        for slot in remaining:
            valid = [
                option
                for option in options[slot]
                if not used >> option[0] & 1 and not option[1] & occupied
            ]
            choices.append((len(valid), slot, valid))
        coverage = occupied
        for _, _, valid in choices:
            for option in valid:
                coverage |= option[1]
        if coverage != full:
            failed.add(state)
            return None
        _, slot, valid = min(choices, key=lambda item: item[0])
        for option in valid:
            answer = search(
                [other for other in remaining if other != slot],
                used | 1 << option[0],
                occupied | option[1],
                chosen + [(slot, option)],
            )
            if answer is not None:
                return answer
        failed.add(state)
        return None

    return search(list(options), 0, 0, [])


def solve(grid):
    palette, top, left = _find_palette(grid)
    rows, cols = len(palette), len(palette[0])
    shapes = _extract_shapes(grid, top, left, rows)
    if len(shapes) != rows * cols:
        raise ValueError("task assumptions are not satisfied")
    size = math.ceil(math.sqrt(sum(sum(row) for shape in shapes for row in shape)))
    answer = _exact_cover(_placement_options(shapes, rows, cols, size), size)
    if answer is None:
        raise ValueError("task assumptions are not satisfied")
    output = [[0] * size for _ in range(size)]
    for slot, (_, _, cells) in answer:
        for row, col in cells:
            output[row][col] = palette[slot // cols][slot % cols]
    return output
