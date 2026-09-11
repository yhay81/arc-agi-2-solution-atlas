def solve(grid):
    h, w = len(grid), len(grid[0])
    matches = []
    for color in sorted({value for row in grid for value in row if value}):
        if color == 0:
            continue
        cells = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == color]
        for component in [cells]:
            rows = [row for row, _ in component]
            cols = [col for _, col in component]
            top, bottom, left, right = min(rows), max(rows), min(cols), max(cols)
            if bottom - top < 2 or right - left < 2:
                continue
            if not (
                all(grid[top][c] == color for c in range(left, right + 1))
                and all(grid[bottom][c] == color for c in range(left, right + 1))
                and all(grid[r][left] == color for r in range(top, bottom + 1))
                and all(grid[r][right] == color for r in range(top, bottom + 1))
            ):
                continue
            if not any(
                grid[r][c] != color for r in range(top + 1, bottom) for c in range(left + 1, right)
            ):
                continue
            matches.append(color)
    if len(matches) != 1:
        return [row[:] for row in grid]
    return [[matches[0]]]
