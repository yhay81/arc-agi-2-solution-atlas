def solve(grid):
    height, width = len(grid), len(grid[0])
    marker_color = 2
    separator_color = 8
    output = [row[:] for row in grid]
    separator_rows = [
        row for row in range(height) if all(value == separator_color for value in grid[row])
    ]
    separator_cols = [
        col
        for col in range(width)
        if all(grid[row][col] == separator_color for row in range(height))
    ]
    if bool(separator_rows) == bool(separator_cols):
        return output
    markers = [(r, c) for r in range(height) for c in range(width) if grid[r][c] == marker_color]
    if not len(markers):
        return output
    if separator_rows:
        for marker_row, marker_col in markers:
            if marker_row in separator_rows:
                continue
            targets = (
                [separator_rows[0]]
                if marker_row < separator_rows[0]
                else [separator_rows[-1]]
                if marker_row > separator_rows[-1]
                else [
                    row
                    for row in (
                        max((row for row in separator_rows if row < marker_row), default=None),
                        min((row for row in separator_rows if row > marker_row), default=None),
                    )
                    if row is not None
                ]
            )
            for separator_row in targets:
                start, stop = sorted((marker_row, separator_row))
                for row in range(start, stop + 1):
                    output[row][marker_col] = marker_color
                for row in range(separator_row - 1, separator_row + 2):
                    for col in range(marker_col - 1, marker_col + 2):
                        if 0 <= row < height and 0 <= col < width:
                            output[row][col] = (
                                marker_color
                                if (row, col) == (separator_row, marker_col)
                                else separator_color
                            )
    else:
        for marker_row, marker_col in markers:
            if marker_col in separator_cols:
                continue
            targets = (
                [separator_cols[0]]
                if marker_col < separator_cols[0]
                else [separator_cols[-1]]
                if marker_col > separator_cols[-1]
                else [
                    col
                    for col in (
                        max((col for col in separator_cols if col < marker_col), default=None),
                        min((col for col in separator_cols if col > marker_col), default=None),
                    )
                    if col is not None
                ]
            )
            for separator_col in targets:
                start, stop = sorted((marker_col, separator_col))
                output[marker_row][start : stop + 1] = [marker_color] * (stop - start + 1)
                for row in range(marker_row - 1, marker_row + 2):
                    for col in range(separator_col - 1, separator_col + 2):
                        if 0 <= row < height and 0 <= col < width:
                            output[row][col] = (
                                marker_color
                                if (row, col) == (marker_row, separator_col)
                                else separator_color
                            )
    return output
