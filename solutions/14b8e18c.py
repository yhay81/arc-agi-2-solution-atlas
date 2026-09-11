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
            if grid[row][col] == background or (row, col) in seen:
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
                        and grid[rr][cc] != background
                        and (rr, cc) not in seen
                    ):
                        seen.add((rr, cc))
                        stack.append((rr, cc))
            components.append(cells)
    output = [row[:] for row in grid]
    for component in components:
        if len(component) < 4:
            continue
        rows = [r for r, _ in component]
        cols = [c for _, c in component]
        top, bottom, left, right = min(rows), max(rows), min(cols), max(cols)
        if bottom - top != right - left:
            continue
        points = set(component)
        border = (
            {(top, c) for c in range(left, right + 1)}
            | {(bottom, c) for c in range(left, right + 1)}
            | {(r, left) for r in range(top, bottom + 1)}
            | {(r, right) for r in range(top, bottom + 1)}
        )
        full = {(r, c) for r in range(top, bottom + 1) for c in range(left, right + 1)}
        if points not in (full, border):
            continue
        for row, col in (
            (top - 1, left),
            (top - 1, right),
            (top, left - 1),
            (top, right + 1),
            (bottom, left - 1),
            (bottom, right + 1),
            (bottom + 1, left),
            (bottom + 1, right),
        ):
            if 0 <= row < height and 0 <= col < width and grid[row][col] == background:
                output[row][col] = 2
    return output
