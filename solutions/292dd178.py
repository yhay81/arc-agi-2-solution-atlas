def solve(grid):
    height, width = len(grid), len(grid[0])
    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = max(counts, key=lambda value: (counts[value], -value))
    seen = set()
    components = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] != 1 or (row, col) in seen:
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
                        and grid[rr][cc] == 1
                        and (rr, cc) not in seen
                    ):
                        seen.add((rr, cc))
                        stack.append((rr, cc))
            components.append(cells)
    output = [row[:] for row in grid]
    for cells in components:
        if len(cells) < 4:
            continue
        top, bottom = min(r for r, _ in cells), max(r for r, _ in cells)
        left, right = min(c for _, c in cells), max(c for _, c in cells)
        if bottom - top < 2 or right - left < 2:
            continue
        for row in range(top + 1, bottom):
            for col in range(left + 1, right):
                if grid[row][col] == background:
                    output[row][col] = 2
        openings = []
        for col in range(left + 1, right):
            if grid[top][col] == background:
                openings.append((top, col, -1, 0))
            if grid[bottom][col] == background:
                openings.append((bottom, col, 1, 0))
        for row in range(top + 1, bottom):
            if grid[row][left] == background:
                openings.append((row, left, 0, -1))
            if grid[row][right] == background:
                openings.append((row, right, 0, 1))
        for row, col, dr, dc in openings:
            output[row][col] = 2
            rr, cc = row + dr, col + dc
            while 0 <= rr < height and 0 <= cc < width and grid[rr][cc] == background:
                output[rr][cc] = 2
                rr += dr
                cc += dc
    return output
