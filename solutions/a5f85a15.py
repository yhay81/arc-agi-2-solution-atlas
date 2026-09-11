def _recolor_nonzero_odd_rows(array):
    values = {value for row in array for value in row if value != 0}
    if len(values) != 1:
        return [row[:] for row in array]
    output = [row[:] for row in array]
    positions = [(r, c) for r, row in enumerate(array) for c, v in enumerate(row) if v != 0]
    changed = False
    for sign in (1, -1):
        groups: dict[int, list[tuple[int, int]]] = {}
        for row, col in positions:
            key = row - sign * col
            groups.setdefault(key, []).append((row, col))
        for cells in groups.values():
            cells.sort()
            start = 0
            for index in range(1, len(cells) + 1):
                if index == len(cells) or cells[index][0] != cells[index - 1][0] + 1:
                    run = cells[start:index]
                    if len(run) >= 2:
                        for row, col in run[1::2]:
                            output[row][col] = 4
                            changed = True
                    start = index
    return output if changed else [row[:] for row in array]


def solve(grid):
    return _recolor_nonzero_odd_rows([row[:] for row in grid])
