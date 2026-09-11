from itertools import pairwise, permutations


def solve(grid):
    source = [row[:] for row in grid]
    height, width = len(source), len(source[0]) if source else 0
    if height < 3 or width < 2:
        return source
    if len(set(source[-1])) != 1 or source[-1][0] == 0:
        return source
    floor = source[-1][0]
    marker_row = height - 2
    markers = [col for col, value in enumerate(source[marker_row]) if value == floor]
    slots = [
        (left + 1, right - 1)
        for left, right in pairwise(markers)
        if right > left + 1 and all(value == 0 for value in source[marker_row][left + 1 : right])
    ]
    if len(markers) < 2 or not slots:
        return source

    objects = []
    for color in sorted({value for row in source for value in row} - {0, floor}):
        seen = set()
        for row in range(marker_row):
            for col in range(width):
                if source[row][col] != color or (row, col) in seen:
                    continue
                stack = [(row, col)]
                seen.add((row, col))
                cells = []
                while stack:
                    current_row, current_col = stack.pop()
                    cells.append((current_row, current_col))
                    for next_row, next_col in (
                        (current_row - 1, current_col),
                        (current_row + 1, current_col),
                        (current_row, current_col - 1),
                        (current_row, current_col + 1),
                    ):
                        if (
                            0 <= next_row < marker_row
                            and 0 <= next_col < width
                            and source[next_row][next_col] == color
                            and (next_row, next_col) not in seen
                        ):
                            seen.add((next_row, next_col))
                            stack.append((next_row, next_col))
                rows = [row for row, _ in cells]
                cols = [col for _, col in cells]
                top, bottom = min(rows), max(rows)
                left, right = min(cols), max(cols)
                shape = [source[row][left : right + 1] for row in range(top, bottom + 1)]
                if len(cells) != sum(len(row) for row in shape):
                    return source
                if any(value != color for row in shape for value in row):
                    return source
                objects.append((color, [row[:] for row in shape]))
    if len(objects) != len(slots):
        return source

    options = []
    for left, right in slots:
        slot_width = right - left + 1
        matches = []
        for object_index, (_, shape) in enumerate(objects):
            if len(shape[0]) == slot_width:
                matches.append((object_index, shape))
            elif len(shape) == slot_width and len(shape) != len(shape[0]):
                matches.append((object_index, [list(row) for row in zip(*shape[::-1])]))
        options.append(matches)

    assignments = []
    for order in permutations(range(len(objects))):
        chosen = []
        for slot, object_index in zip(options, order):
            match = next((shape for index, shape in slot if index == object_index), None)
            if match is None:
                break
            chosen.append(match)
        else:
            assignments.append(chosen)
            if len(assignments) > 1:
                return source
    if len(assignments) != 1:
        return source

    output = [[0] * width for _ in range(height)]
    for col, value in enumerate(source[marker_row]):
        if value == floor:
            output[marker_row][col] = floor
    output[-1] = [floor] * width
    for (left, right), shape in zip(slots, assignments[0]):
        rows, cols = len(shape), len(shape[0])
        if cols != right - left + 1 or rows > marker_row:
            return source
        top = marker_row - rows + 1
        for row, values in enumerate(shape, top):
            output[row][left : right + 1] = values
    return output
