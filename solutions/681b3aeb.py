def solve(grid):
    height, width = len(grid), len(grid[0])
    colors = {value for row in grid for value in row if value != 0}
    pieces = []
    for color in sorted(colors):
        seen = set()
        groups = []
        for row in range(height):
            for col in range(width):
                if grid[row][col] != color or (row, col) in seen:
                    continue
                stack = [(row, col)]
                seen.add((row, col))
                cells = []
                while stack:
                    r, c = stack.pop()
                    cells.append((r, c))
                    for rr, cc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                        if (
                            0 <= rr < height
                            and 0 <= cc < width
                            and grid[rr][cc] == color
                            and (rr, cc) not in seen
                        ):
                            seen.add((rr, cc))
                            stack.append((rr, cc))
                groups.append(cells)
        if len(groups) != 1:
            return [row[:] for row in grid]
        cells = groups[0]
        top, left = min(r for r, _ in cells), min(c for _, c in cells)
        bottom, right = max(r for r, _ in cells), max(c for _, c in cells)
        shape = [row[left : right + 1] for row in grid[top : bottom + 1]]
        pieces.append((color, shape))
    if len(pieces) != 2 or any(len(shape) > 3 or len(shape[0]) > 3 for _, shape in pieces):
        return [row[:] for row in grid]
    layouts = []
    for first_row in range(4 - len(pieces[0][1])):
        for first_col in range(4 - len(pieces[0][1][0])):
            for second_row in range(4 - len(pieces[1][1])):
                for second_col in range(4 - len(pieces[1][1][0])):
                    output = [[0] * 3 for _ in range(3)]
                    valid = True
                    for color, shape, row0, col0 in (
                        (pieces[0][0], pieces[0][1], first_row, first_col),
                        (pieces[1][0], pieces[1][1], second_row, second_col),
                    ):
                        for r, line in enumerate(shape):
                            for c, value in enumerate(line):
                                if not value:
                                    continue
                                if output[row0 + r][col0 + c]:
                                    valid = False
                                output[row0 + r][col0 + c] = color
                    if valid:
                        layouts.append(output)
    return layouts[0] if len(layouts) == 1 else [row[:] for row in grid]
