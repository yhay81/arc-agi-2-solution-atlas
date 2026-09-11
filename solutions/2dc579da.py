def _overlay_four_quadrants_unique(array):
    height, width = len(array), len(array[0])
    if height % 2 == 0 or width % 2 == 0:
        return [r[:] for r in array]
    mid_row, mid_col = (height // 2, width // 2)
    separator = array[mid_row][mid_col]
    if any(v != separator for v in array[mid_row]) or any(
        array[r][mid_col] != separator for r in range(height)
    ):
        return [r[:] for r in array]
    panels = (
        [r[:mid_col] for r in array[:mid_row]],
        [r[mid_col + 1 :] for r in array[:mid_row]],
        [r[:mid_col] for r in array[mid_row + 1 :]],
        [r[mid_col + 1 :] for r in array[mid_row + 1 :]],
    )
    output = [[0] * mid_col for _ in range(mid_row)]
    for row in range(mid_row):
        for col in range(mid_col):
            values = [panel[row][col] for panel in panels]
            counts = {value: values.count(value) for value in set(values)}
            unique = [value for value, count in counts.items() if count == 1]
            output[row][col] = (
                unique[0] if len(unique) == 1 else max(counts, key=lambda value: counts[value])
            )
    return output


def solve(grid):
    return _overlay_four_quadrants_unique(grid)
