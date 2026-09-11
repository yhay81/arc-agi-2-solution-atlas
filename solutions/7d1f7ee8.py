def solve(grid):
    if not grid or not grid[0]:
        return grid
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = max(counts, key=counts.get)
    seen = set()
    frames = []
    for row in range(height):
        for col in range(width):
            color = grid[row][col]
            if color == background or (row, col) in seen:
                continue
            cells = []
            stack = [(row, col)]
            seen.add((row, col))
            while stack:
                current_row, current_col = stack.pop()
                cells.append((current_row, current_col))
                for next_row, next_col in (
                    (current_row - 1, current_col),
                    (current_row + 1, current_col),
                    (current_row, current_col - 1),
                    (current_row, current_col + 1),
                ):
                    if (
                        0 <= next_row < height
                        and 0 <= next_col < width
                        and grid[next_row][next_col] == color
                        and (next_row, next_col) not in seen
                    ):
                        seen.add((next_row, next_col))
                        stack.append((next_row, next_col))
            if len(cells) < 8:
                continue
            top = min(row for row, _ in cells)
            bottom = max(row for row, _ in cells)
            left = min(col for _, col in cells)
            right = max(col for _, col in cells)
            if bottom - top < 2 or right - left < 2:
                continue
            border = (
                all(grid[top][col] == color for col in range(left, right + 1))
                and all(grid[bottom][col] == color for col in range(left, right + 1))
                and all(grid[row][left] == color for row in range(top, bottom + 1))
                and all(grid[row][right] == color for row in range(top, bottom + 1))
            )
            if border and not any(top < row < bottom and left < col < right for row, col in cells):
                frames.append((top, bottom, left, right, color))
    for row in range(height):
        for col in range(width):
            if grid[row][col] == background:
                continue
            containing = [
                frame for frame in frames if frame[0] < row < frame[1] and frame[2] < col < frame[3]
            ]
            if containing:
                frame = max(containing, key=lambda item: (item[1] - item[0]) * (item[3] - item[2]))
                output[row][col] = frame[4]
    return output
