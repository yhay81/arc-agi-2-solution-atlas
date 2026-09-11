def _project_plus_marker_rays(array):
    output = [row[:] for row in array]
    height, width = len(array), len(array[0])
    markers: list[tuple[int, int, int, set[tuple[int, int]]]] = []
    for row in range(1, height - 1):
        for col in range(1, width - 1):
            arm_values = (
                array[row - 1][col],
                array[row + 1][col],
                array[row][col - 1],
                array[row][col + 1],
            )
            if len(set(arm_values)) != 1 or arm_values[0] == 0:
                continue
            center = array[row][col]
            if center != arm_values[0]:
                markers.append(
                    (
                        row,
                        col,
                        center,
                        {
                            (row, col),
                            (row - 1, col),
                            (row + 1, col),
                            (row, col - 1),
                            (row, col + 1),
                        },
                    )
                )
    if not markers:
        return output
    inactive_rows = {row for row, _col, color, _cells in markers if color == 0}
    inactive_cols = {col for _row, col, color, _cells in markers if color == 0}
    marker_cells = set().union(*(cells for _row, _col, _color, cells in markers))
    for orientation in ("vertical", "horizontal"):
        for row, col, color, own_cells in markers:
            if color == 0:
                continue
            for direction in (-1, 1):
                distance = 1
                while True:
                    target_row = row + direction * distance if orientation == "vertical" else row
                    target_col = col if orientation == "vertical" else col + direction * distance
                    if not (0 <= target_row < height and 0 <= target_col < width):
                        break
                    if orientation == "vertical" and target_col in inactive_cols:
                        distance += 1
                        continue
                    if orientation == "horizontal" and (
                        target_col in inactive_cols or target_row in inactive_rows
                    ):
                        distance += 1
                        continue
                    target = (target_row, target_col)
                    if target in marker_cells and target not in own_cells:
                        break
                    if array[target_row][target_col] == 0 and output[target_row][target_col] == 0:
                        output[target_row][target_col] = color
                    distance += 1
    return output


def solve(grid):
    return _project_plus_marker_rays(grid)
