from collections import Counter


def solve(grid):
    height, width = len(grid), len(grid[0])
    counts = Counter(value for row in grid for value in row)
    background = next(value for value in counts if counts[value] == max(counts.values()))
    row_separators = [
        row for row in range(height) if len(set(grid[row])) == 1 and grid[row][0] != background
    ]
    col_separators = [
        col
        for col in range(width)
        if len({grid[row][col] for row in range(height)}) == 1 and grid[0][col] != background
    ]
    if not row_separators or not col_separators:
        return [row[:] for row in grid]
    separator_colors = {grid[row][0] for row in row_separators}
    separator_colors.update(grid[0][col] for col in col_separators)
    if len(separator_colors) != 1:
        return [row[:] for row in grid]
    separator = next(iter(separator_colors))
    row_edges, col_edges = ([-1, *row_separators, height], [-1, *col_separators, width])
    cells = []
    for i in range(len(row_edges) - 1):
        top, bottom = row_edges[i : i + 2]
        for j in range(len(col_edges) - 1):
            left, right = col_edges[j : j + 2]
            cell_top, cell_left = (top + 1, left + 1)
            region = [row[cell_left:right] for row in grid[cell_top:bottom]]
            if not region or not region[0]:
                return [row[:] for row in grid]
            colors = [
                value
                for value in {value for row in region for value in row}
                if value not in (background, separator)
            ]
            if len(colors) > 1:
                return [row[:] for row in grid]
            marker = colors[0] if colors else background
            count = sum(value == marker for row in region for value in row) if colors else 0
            cells.append((cell_top, bottom, cell_left, right, marker, count))
    maximum = max((count for *_, count in cells))
    output = [row[:] for row in grid]
    for cell_top, cell_bottom, cell_left, cell_right, marker, count in cells:
        fill = marker if marker != background and count == maximum else background
        for row in range(cell_top, cell_bottom):
            output[row][cell_left:cell_right] = [fill] * (cell_right - cell_left)
    return output
