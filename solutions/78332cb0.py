from collections import Counter
from itertools import permutations


def solve(grid):
    height, width = len(grid), len(grid[0])
    colors = {cell for row in grid for cell in row}
    full_rows = [[all(cell == color for cell in row) for row in grid] for color in colors]
    full_cols = [
        [all(grid[row][col] == color for row in range(height)) for col in range(width)]
        for color in colors
    ]
    separators = [
        color
        for color, rows, cols in zip(colors, full_rows, full_cols, strict=True)
        if any(rows) or any(cols)
    ]
    separator = 6 if 6 in separators else (separators[0] if separators else 6)
    row_separators = [all(cell == separator for cell in row) for row in grid]
    col_separators = [
        all(grid[row][col] == separator for row in range(height)) for col in range(width)
    ]
    row_ranges = []
    start = 0
    for end, is_separator in enumerate(row_separators + [True]):
        if is_separator:
            if start < end:
                row_ranges.append((start, end))
            start = end + 1
    col_ranges = []
    start = 0
    for end, is_separator in enumerate(col_separators + [True]):
        if is_separator:
            if start < end:
                col_ranges.append((start, end))
            start = end + 1
    blocks = [
        [row[col_start:col_end] for row in grid[row_start:row_end]]
        for row_start, row_end in row_ranges
        for col_start, col_end in col_ranges
    ]
    background = Counter(cell for block in blocks for row in block for cell in row).most_common(1)[
        0
    ][0]
    solutions = []
    for axis in (0, 1):
        edges = [
            (
                [cell != background for cell in block[0]],
                [cell != background for cell in block[-1]],
            )
            if axis == 0
            else (
                [row[0] != background for row in block],
                [row[-1] != background for row in block],
            )
            for block in blocks
        ]
        for order in permutations(range(len(blocks))):
            if any(edges[order[0]][0]) or any(edges[order[-1]][1]):
                continue
            if all(any(edges[order[i]][1]) for i in range(len(order) - 1)) and all(
                edges[order[i]][1] == edges[order[i + 1]][0] for i in range(len(order) - 1)
            ):
                solutions.append((axis, order))
    if not (len(solutions) == 1):
        raise ValueError("task assumptions are not satisfied")
    axis, order = solutions[0]
    if axis == 0:
        output = []
        for index, block_index in enumerate(order):
            if index:
                output.append([separator] * len(blocks[block_index][0]))
            output.extend(row[:] for row in blocks[block_index])
        return output
    output = [[] for _ in blocks[order[0]]]
    for index, block_index in enumerate(order):
        if index:
            for row in output:
                row.append(separator)
        for row_index, row in enumerate(blocks[block_index]):
            output[row_index].extend(row)
    return output
