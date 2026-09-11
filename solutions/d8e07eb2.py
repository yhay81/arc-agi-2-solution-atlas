from collections import Counter


def _runs(indices):
    result = []
    for index in indices:
        if not result or index > result[-1][-1] + 1:
            result.append([index])
        else:
            result[-1].append(index)
    return [(run[0], run[-1]) for run in result]


def solve(grid):
    height, width = len(grid), len(grid[0])
    background = Counter(value for row in grid for value in row).most_common(1)[0][0]
    dividers = [
        row for row, values in enumerate(grid) if len(set(values)) == 1 and values[0] != background
    ]
    content_rows = [
        row
        for row, values in enumerate(grid)
        if row not in dividers and any(value != background for value in values)
    ]
    row_blocks = _runs(content_rows)
    content_cols = [
        col
        for col in range(width)
        if any(
            grid[row][col] != background
            for top, bottom in row_blocks
            for row in range(top, bottom + 1)
        )
    ]
    col_blocks = _runs(content_cols)
    if len(row_blocks) < 2 or not col_blocks:
        raise ValueError("task assumptions are not satisfied")

    def patch(row_block, col_block):
        top, bottom = row_block
        left, right = col_block
        return tuple(tuple(grid[row][left : right + 1]) for row in range(top, bottom + 1))

    header = {
        patch(row_blocks[0], col_block)
        for col_block in col_blocks
        if any(
            grid[row][col] != background
            for row in range(row_blocks[0][0], row_blocks[0][1] + 1)
            for col in range(col_block[0], col_block[1] + 1)
        )
    }
    selected = {
        (row_index, col_index)
        for row_index, row_block in enumerate(row_blocks[1:])
        for col_index, col_block in enumerate(col_blocks)
        if patch(row_block, col_block) in header
    }
    complete = any(
        all((row, col) in selected for col in range(len(col_blocks)))
        for row in range(len(row_blocks) - 1)
    ) or any(
        all((row, col) in selected for row in range(len(row_blocks) - 1))
        for col in range(len(col_blocks))
    )

    output = [row[:] for row in grid]
    for row_index, col_index in selected:
        top, bottom = row_blocks[row_index + 1]
        left, right = col_blocks[col_index]
        for row in range(top - 1, bottom + 2):
            for col in range(left - 1, right + 2):
                if output[row][col] == background:
                    output[row][col] = 3
    if complete:
        for row in range(row_blocks[0][0] - 1, row_blocks[0][1] + 2):
            for col in range(width):
                if output[row][col] == background:
                    output[row][col] = 3
    for row in range(dividers[-1] + 1, height):
        for col in range(width):
            if output[row][col] == background:
                output[row][col] = 3 if complete else 2
    return output
