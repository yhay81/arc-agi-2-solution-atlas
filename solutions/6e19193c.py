def solve(grid):
    height, width = len(grid), len(grid[0])
    seen = set()
    components = []
    for row in range(height):
        for col in range(width):
            if not grid[row][col] or (row, col) in seen:
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
                        and grid[rr][cc]
                        and (rr, cc) not in seen
                    ):
                        seen.add((rr, cc))
                        stack.append((rr, cc))
            components.append(cells)
    output = [row[:] for row in grid]
    for cells in components:
        rows = [r for r, _ in cells]
        cols = [c for _, c in cells]
        top, bottom, left, right = min(rows), max(rows), min(cols), max(cols)
        if len(cells) != 3 or bottom - top != 1 or right - left != 1:
            return [row[:] for row in grid]
        colors = {grid[r][c] for r, c in cells}
        if len(colors) != 1:
            return [row[:] for row in grid]
        missing = next((r, c) for r in (top, bottom) for c in (left, right) if (r, c) not in cells)
        dr = -1 if missing[0] == top else 1
        dc = -1 if missing[1] == left else 1
        r, c = missing[0] + dr, missing[1] + dc
        color = next(iter(colors))
        while 0 <= r < height and 0 <= c < width:
            if output[r][c] == 0:
                output[r][c] = color
            r += dr
            c += dc
    return output
