def _symmetrize(array, mode):
    output = [row[:] for row in array]
    if mode == "lr":
        mirrored = [list(reversed(row)) for row in array]
    elif mode == "ud":
        mirrored = list(reversed(array))
    elif mode == "diag" and len(array) == len(array[0]):
        mirrored = [[array[c][r] for c in range(len(array))] for r in range(len(array))]
    else:
        return array.copy()
    output = [
        [value if value != 0 else mirrored[r][c] for c, value in enumerate(row)]
        for r, row in enumerate(output)
    ]
    return output


def solve(grid):
    return _symmetrize(grid, "ud")
