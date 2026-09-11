def solve(grid):
    height, width = len(grid), len(grid[0])
    seen = set()
    rectangles = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] == 0 or (row, col) in seen:
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
            top = min(r for r, _ in cells)
            bottom = max(r for r, _ in cells)
            left = min(c for _, c in cells)
            right = max(c for _, c in cells)
            if bottom - top < 2 or right - left < 2:
                return [row[:] for row in grid]
            if len(cells) != (bottom - top + 1) * (right - left + 1):
                return [row[:] for row in grid]
            rectangles.append((top, bottom, left, right))
    if len(rectangles) != 2:
        return [row[:] for row in grid]
    areas = [(bottom - top + 1) * (right - left + 1) for top, bottom, left, right in rectangles]
    if areas[0] == areas[1]:
        return [row[:] for row in grid]
    smaller = areas.index(min(areas))
    output = [row[:] for row in grid]
    for index, (top, bottom, left, right) in enumerate(rectangles):
        color = 1 if index == smaller else 2
        for row in range(top + 1, bottom):
            for col in range(left + 1, right):
                output[row][col] = color
    return output
