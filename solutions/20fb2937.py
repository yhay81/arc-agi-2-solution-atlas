def _substitute_from_header(array, partition_color=6):
    h, w = len(array), len(array[0])
    separators = [row for row in range(h) if all(v == partition_color for v in array[row])]
    if not separators:
        return [row[:] for row in array]
    separator = separators[0]
    header, work = (array[:separator], array[separator + 1 :])
    if len(header) < 5 or len(work) < 3:
        return [row[:] for row in array]
    mapping: dict[int, np.ndarray] = {}
    for left in range(0, w - 2, 4):
        block = [row[left : left + 3] for row in header[:3]]
        if len(block) != 3 or any(len(row) != 3 for row in block):
            continue
        value = header[4][left + 1] if len(header) > 4 else 0
        mapping[value] = block
    if not mapping:
        return [row[:] for row in array]
    background = max(
        {v for row in work for v in row}, key=lambda v: sum(x == v for row in work for x in row)
    )
    output = [[background] * w for _ in work]
    for row in range(len(work)):
        for col in range(w):
            if work[row][col] not in mapping:
                continue
            value = work[row][col]
            if row < 1 or row + 1 >= len(work):
                continue
            block = mapping[value]
            top, left = row - 1, col - 1
            for dr in range(3):
                for dc in range(3):
                    target_row, target_col = (top + dr, left + dc)
                    if 0 <= target_row < len(output) and 0 <= target_col < w:
                        output[target_row][target_col] = block[dr][dc]
    return output


def solve(grid):
    return _substitute_from_header([row[:] for row in grid], 6)
