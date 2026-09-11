def solve(grid):
    cells = [(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == 5]
    if not cells:
        return [row[:] for row in grid]
    top, left = min(r for r, _ in cells), min(c for _, c in cells)
    bottom, right = max(r for r, _ in cells), max(c for _, c in cells)
    mask = [row[left : right + 1] for row in grid[top : bottom + 1]]
    width = right - left + 1
    keys = []
    for r in range(len(grid) - 2):
        for c in range(len(grid[0]) - width + 1):
            first, second, fallback = (
                grid[r][c : c + width],
                grid[r + 1][c : c + width],
                grid[r + 2][c : c + width],
            )
            if (
                min(first) != 0
                and first == second
                and len(set(fallback)) == 1
                and fallback[0] != 0
                and first != fallback
            ):
                keys.append((first[:], fallback[0]))
    if len(keys) != 1:
        return [row[:] for row in grid]
    palette, fallback = keys[0]
    return [[palette[c] if value == 5 else fallback for c, value in enumerate(row)] for row in mask]
