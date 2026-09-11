def _select_densest_square_panel(array):
    h, w = len(array), len(array[0])
    if w % h == 0:
        size = h
        panels = [[row[col : col + size] for row in array] for col in range(0, w, size)]
    elif h % w == 0:
        size = w
        panels = [array[row : row + size] for row in range(0, h, size)]
    else:
        return array.copy()
    counts = [sum(v != 0 for row in panel for v in row) for panel in panels]
    return (
        panels[counts.index(max(counts))]
        if counts.count(max(counts)) == 1
        else [row[:] for row in array]
    )


def solve(grid):
    return _select_densest_square_panel(grid)
