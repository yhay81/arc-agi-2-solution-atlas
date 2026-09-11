def solve(grid):
    if not grid or not grid[0]:
        return [row[:] for row in grid]
    height, width = len(grid), len(grid[0])
    values = sorted({value for row in grid for value in row})
    counts = {value: sum(row.count(value) for row in grid) for value in values}
    background = min(values, key=lambda value: (-counts[value], value))
    colours = [value for value in values if value != background]
    if not colours:
        return [row[:] for row in grid]
    colours.sort(
        key=lambda value: min(
            col for row in range(height) for col in range(width) if grid[row][col] == value
        )
    )
    output = [[background] * width for _ in range(height)]
    lane_left = 0
    for colour in colours:
        seen = set()
        pieces = []
        for row in range(height):
            for col in range(width):
                if grid[row][col] != colour or (row, col) in seen:
                    continue
                stack = [(row, col)]
                seen.add((row, col))
                cells = []
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
                            and grid[next_row][next_col] == colour
                            and (next_row, next_col) not in seen
                        ):
                            seen.add((next_row, next_col))
                            stack.append((next_row, next_col))
                pieces.append(cells)
        pieces.sort(key=lambda cells: min(col for _, col in cells))
        cursor = height - 1
        lane_width = 0
        for cells in pieces:
            rows = [row for row, _ in cells]
            columns = [col for _, col in cells]
            top, bottom = min(rows), max(rows)
            left, right = min(columns), max(columns)
            piece_height, piece_width = bottom - top + 1, right - left + 1
            start = cursor - piece_height + 1
            if start < 0 or lane_left + piece_width > width:
                return [row[:] for row in grid]
            for piece_row in range(piece_height):
                for piece_col in range(piece_width):
                    output[start + piece_row][lane_left + piece_col] = (
                        colour if grid[top + piece_row][left + piece_col] == colour else background
                    )
            cursor = start - 2
            lane_width = max(lane_width, piece_width)
        lane_left += lane_width + 1
    return output
