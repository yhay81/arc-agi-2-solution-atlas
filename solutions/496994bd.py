def _symmetrize(array, mode):
    output = [row[:] for row in array]
    if mode == "lr":
        mirrored = [row[::-1] for row in array]
    elif mode == "ud":
        mirrored = array[::-1]
    elif mode == "diag" and len(array) == len(array[0]):
        mirrored = [list(col) for col in zip(*array)]
    else:
        return array.copy()
    output = [
        [v if v != 0 else mirrored[r][c] for c, v in enumerate(row)] for r, row in enumerate(output)
    ]
    return output


def solve(grid):
    return _symmetrize(grid, "ud")
