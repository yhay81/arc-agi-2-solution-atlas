def solve(grid):
    height, width = len(grid), len(grid[0])
    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = max(counts, key=counts.get)
    colors = [value for value in counts if value != background]
    if not colors:
        return [row[:] for row in grid]
    separator = max(
        colors,
        key=lambda color: max(
            [sum(value == color for value in row) for row in grid]
            + [sum(grid[r][c] == color for r in range(height)) for c in range(width)]
        ),
    )
    rows = [
        r for r, row in enumerate(grid) if sum(value == separator for value in row) * 10 > width * 7
    ]
    cols = [
        c
        for c in range(width)
        if sum(grid[r][c] == separator for r in range(height)) * 10 > height * 7
    ]
    rectangles = []
    for top_index, top in enumerate(rows):
        for bottom in rows[top_index + 1 :]:
            for left_index, left in enumerate(cols):
                for right in cols[left_index + 1 :]:
                    if any(
                        grid[r][c] == separator
                        for r, c in ((top, left), (top, right), (bottom, left), (bottom, right))
                    ):
                        continue
                    border = (
                        [grid[top][c] for c in range(left + 1, right)]
                        + [grid[bottom][c] for c in range(left + 1, right)]
                        + [grid[r][left] for r in range(top + 1, bottom)]
                        + [grid[r][right] for r in range(top + 1, bottom)]
                    )
                    if all(value == separator for value in border):
                        rectangles.append((top, bottom, left, right))
    if len(rectangles) != 1:
        return [row[:] for row in grid]
    top, bottom, left, right = rectangles[0]
    return [row[left : right + 1] for row in grid[top : bottom + 1]]
