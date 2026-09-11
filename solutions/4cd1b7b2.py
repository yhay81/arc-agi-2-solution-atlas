def _latin_fill(array):
    if len(array) != len(array[0]):
        return [row[:] for row in array]
    output = [row[:] for row in array]
    symbols = set(range(1, len(output) + 1))
    changed = True
    while changed:
        changed = False
        for row in range(len(output)):
            for col in range(len(output)):
                if output[row][col] != 0:
                    continue
                options = symbols - set(output[row]) - {output[r][col] for r in range(len(output))}
                if len(options) == 1:
                    output[row][col] = options.pop()
                    changed = True
    return output


def solve(grid):
    return _latin_fill(grid)
