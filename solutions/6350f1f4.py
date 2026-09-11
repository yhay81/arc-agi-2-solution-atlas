def _normalize_partitioned_blocks(array):
    if not array or not array[0]:
        return [row[:] for row in array]
    cleaned = [[0 if v == 5 else v for v in row] for row in array]
    height, width = len(cleaned), len(cleaned[0])
    separator_row = next((row for row in range(height) if all(v == 0 for v in cleaned[row])), None)
    separator_col = next(
        (col for col in range(width) if all(cleaned[r][col] == 0 for r in range(height))), None
    )
    if separator_row is None or separator_col is None or separator_row != separator_col:
        return [row[:] for row in array]
    size = int(separator_row)
    if size <= 0 or height < size or width < size:
        return [row[:] for row in array]
    starts_row = list(range(0, height, size + 1))
    starts_col = list(range(0, width, size + 1))
    blocks = []
    for top in starts_row:
        for left in starts_col:
            block = [row[left : left + size] for row in cleaned[top : top + size]]
            if len(block) == size and all(len(row) == size for row in block):
                blocks.append((top, left, block))
    reference = next(
        (block for _, _, block in blocks if all(v != 0 for row in block for v in row)), None
    )
    if reference is None:
        return [row[:] for row in array]
    values = {v for row in reference for v in row}
    dominant = max(values, key=lambda v: sum(x == v for row in reference for x in row))
    output = [row[:] for row in cleaned]
    for top, left, block in blocks:
        if any(v == dominant for row in block for v in row):
            for r in range(top, top + size):
                output[r][left : left + size] = [dominant] * size
        else:
            for r in range(size):
                output[top + r][left : left + size] = reference[r]
    return output


def solve(grid):
    return _normalize_partitioned_blocks([row[:] for row in grid])
