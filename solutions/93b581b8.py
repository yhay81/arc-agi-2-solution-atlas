def _satellite_blocks(array):
    positions = [(r, c) for r, row in enumerate(array) for c, v in enumerate(row) if v != 0]
    if len(positions) != 4:
        return [row[:] for row in array]
    top = min(r for r, _ in positions)
    left = min(c for _, c in positions)
    bottom = max(r for r, _ in positions)
    right = max(c for _, c in positions)
    if (bottom - top, right - left) != (1, 1):
        return [row[:] for row in array]
    block = [row[left : right + 1] for row in array[top : bottom + 1]]
    output = [row[:] for row in array]
    placements = (
        (top - 2, left - 2, block[1][1]),
        (top - 2, left + 2, block[1][0]),
        (top + 2, left - 2, block[0][1]),
        (top + 2, left + 2, block[0][0]),
    )
    for row, col, color in placements:
        for r in range(max(row, 0), min(row + 2, len(output))):
            for c in range(max(col, 0), min(col + 2, len(output[0]))):
                output[r][c] = color
    return output


def solve(grid):
    return _satellite_blocks(grid)
