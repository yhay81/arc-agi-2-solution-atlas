def solve(grid):
    height, width = len(grid), len(grid[0])
    if height < 3 or width < 3:
        return [row[:] for row in grid]
    nonzero = [
        (value, sum(value == x for row in grid for x in row))
        for value in sorted({x for row in grid for x in row if x})
    ]
    if not nonzero:
        return [row[:] for row in grid]
    frame = max(nonzero, key=lambda item: item[1])[0]
    horizontal = [
        row for row in range(height) if sum(value == frame for value in grid[row]) >= width - 4
    ]
    vertical = [
        col
        for col in range(width)
        if sum(grid[row][col] == frame for row in range(height)) >= height - 3
    ]
    if len(horizontal) < 2 or not vertical:
        return [row[:] for row in grid]
    output = [row[:] for row in grid]
    for i in range(len(horizontal) - 1):
        top, bottom = horizontal[i : i + 2]
        if bottom <= top + 1:
            continue
        edges = [-1, *vertical, width]
        for j in range(len(edges) - 1):
            left, right = edges[j : j + 2]
            start, stop = (max(left + 1, 0), min(right, width))
            if stop <= start:
                continue
            border = [value for value in grid[top][start:stop] if value not in (0, frame)]
            border.extend(value for value in grid[bottom][start:stop] if value not in (0, frame))
            if left >= 0:
                border.extend(
                    grid[row][left]
                    for row in range(top + 1, bottom)
                    if grid[row][left] not in (0, frame)
                )
            if right < width:
                border.extend(
                    grid[row][right]
                    for row in range(top + 1, bottom)
                    if grid[row][right] not in (0, frame)
                )
            if not border:
                continue
            color = max(set(border), key=lambda value: (border.count(value), -value))
            for row in range(top + 1, bottom):
                for col in range(start, stop):
                    if grid[row][col] == 0:
                        output[row][col] = color
    return output
