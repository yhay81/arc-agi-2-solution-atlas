def _expand_row_diagonal(array):
    if len(array) != 1 or not array[0]:
        return [row[:] for row in array]
    motif = array[0]
    count = sum(v != 0 for v in motif)
    if count == 0:
        return [row[:] for row in array]
    side = len(motif) * count
    output = [[0] * side for _ in range(side)]
    for row in range(side):
        offset = side - 1 - row
        left = max(0, offset)
        right = min(side, offset + len(motif))
        motif_left = left - offset
        motif_right = motif_left + (right - left)
        if left < right:
            output[row][left:right] = motif[motif_left:motif_right]
    return output


def solve(grid):
    return _expand_row_diagonal(grid)
