def _consume_ones_into_bounded_gaps(array):
    source = [row[:] for row in array]
    output = [row[:] for row in source]
    supply = [(r, c) for r, row in enumerate(source) for c, v in enumerate(row) if v == 1]
    candidates = []
    for row in range(len(source)):
        col = 0
        while col < len(source[0]):
            if source[row][col] != 0:
                col += 1
                continue
            start = col
            while col < len(source[0]) and source[row][col] == 0:
                col += 1
            end = col - 1
            if start > 0 and col < len(source[0]):
                candidates.extend((row, value) for value in range(start, end + 1))
    removed: list[tuple[int, int]] = []
    for row, col in sorted(candidates, reverse=True):
        if not supply:
            break
        if supply[0][0] <= row:
            source_row, source_col = supply.pop(0)
            output[row][col] = 1
            removed.append((source_row, source_col))
    for row, col in removed:
        output[row][col] = 0
    return output


def solve(grid):
    return _consume_ones_into_bounded_gaps(grid)
