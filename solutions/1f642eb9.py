def solve(grid):
    height, width = len(grid), len(grid[0])
    seen = set()
    components = []
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
                        and grid[rr][cc] != 0
                        and (rr, cc) not in seen
                    ):
                        seen.add((rr, cc))
                        stack.append((rr, cc))
            components.append(cells)
    if len(components) < 2:
        return [row[:] for row in grid]
    largest_size = max(map(len, components))
    bodies = [cells for cells in components if len(cells) == largest_size]
    if len(bodies) != 1:
        return [row[:] for row in grid]
    body = bodies[0]
    body_set = set(body)
    markers = [
        (r, c)
        for r in range(height)
        for c in range(width)
        if grid[r][c] != 0 and (r, c) not in body_set
    ]
    if not markers:
        return [row[:] for row in grid]
    top, bottom = min(r for r, _ in body), max(r for r, _ in body)
    left, right = min(c for _, c in body), max(c for _, c in body)
    body_color = grid[body[0][0]][body[0][1]]
    if len(body) != (bottom - top + 1) * (right - left + 1):
        return [row[:] for row in grid]
    if any(
        grid[r][c] != body_color for r in range(top, bottom + 1) for c in range(left, right + 1)
    ):
        return [row[:] for row in grid]
    output = [row[:] for row in grid]
    for row, col in markers:
        if top <= row <= bottom and col < left:
            target = (row, left)
        elif top <= row <= bottom and col > right:
            target = (row, right)
        elif left <= col <= right and row < top:
            target = (top, col)
        elif left <= col <= right and row > bottom:
            target = (bottom, col)
        else:
            return [row[:] for row in grid]
        output[target[0]][target[1]] = grid[row][col]
    return output
