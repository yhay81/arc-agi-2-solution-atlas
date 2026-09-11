def _overlay_four_quadrants(array, separator=1):
    height, width = len(array), len(array[0])
    if height % 2 == 0 or width % 2 == 0:
        return [row[:] for row in array]
    mid_row, mid_col = (height // 2, width // 2)
    if not all(v == separator for v in array[mid_row]) or not all(
        row[mid_col] == separator for row in array
    ):
        return [row[:] for row in array]
    panels = (
        [row[:mid_col] for row in array[:mid_row]],
        [row[mid_col + 1 :] for row in array[:mid_row]],
        [row[:mid_col] for row in array[mid_row + 1 :]],
        [row[mid_col + 1 :] for row in array[mid_row + 1 :]],
    )
    if len({(len(p), len(p[0])) for p in panels}) != 1:
        return [row[:] for row in array]
    output = [[0] * len(panels[0][0]) for _ in panels[0]]
    for panel in panels:
        for r, row in enumerate(panel):
            for c, v in enumerate(row):
                if output[r][c] == 0:
                    output[r][c] = v
    return output


def solve(grid):
    return _overlay_four_quadrants(grid, 1)
