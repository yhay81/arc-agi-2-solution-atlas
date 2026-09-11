def _reorder_three_panels(array, order=(1, 0, 2)):
    h, w = len(array), len(array[0])
    if h % 3 == 0:
        size = h // 3
        panels = [array[index * size : (index + 1) * size] for index in range(3)]
        output = [[0] * w for _ in range(size)]
        for index in order:
            for r, row in enumerate(panels[index]):
                for c, v in enumerate(row):
                    if v:
                        output[r][c] = v
        return output
    if w % 3 == 0:
        size = w // 3
        panels = [[row[index * size : (index + 1) * size] for row in array] for index in range(3)]
        output = [[0] * size for _ in range(h)]
        for index in order:
            for r, row in enumerate(panels[index]):
                for c, v in enumerate(row):
                    if v:
                        output[r][c] = v
        return output
    return [row[:] for row in array]


def solve(grid):
    return _reorder_three_panels(grid, [1, 0, 2])
