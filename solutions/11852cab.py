def _complete_bbox_rotational_symmetry(array):
    positions = [(r, c) for r, row in enumerate(array) for c, value in enumerate(row) if value != 0]
    if not len(positions):
        return [row[:] for row in array]
    rows, cols = zip(*positions)
    top, left, bottom, right = min(rows), min(cols), max(rows), max(cols)
    patch = [row[left : right + 1] for row in array[top : bottom + 1]]
    if len(patch) != len(patch[0]):
        return [row[:] for row in array]
    completed = [row[:] for row in patch]
    for turns in (1, 2, 3):
        variant = patch
        for _ in range(turns):
            variant = [list(row) for row in zip(*variant[::-1])]
        for r in range(len(completed)):
            for c in range(len(completed)):
                if completed[r][c] == 0:
                    completed[r][c] = variant[r][c]
    output = [row[:] for row in array]
    for r, row in enumerate(completed):
        output[top + r][left : right + 1] = row
    return output


def solve(grid):
    return _complete_bbox_rotational_symmetry(grid)
