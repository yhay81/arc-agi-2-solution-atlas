def solve(grid):
    height, width = len(grid), len(grid[0])
    foreground, marker, replacement = 4, 5, 2
    seen = set()
    components = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] != foreground or (row, col) in seen:
                continue
            stack = [(row, col)]
            seen.add((row, col))
            cells = []
            while stack:
                r, c = stack.pop()
                cells.append((r, c))
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        rr, cc = r + dr, c + dc
                        if (
                            0 <= rr < height
                            and 0 <= cc < width
                            and grid[rr][cc] == foreground
                            and (rr, cc) not in seen
                        ):
                            seen.add((rr, cc))
                            stack.append((rr, cc))
            components.append(cells)
    plus = {(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)}
    output = [row[:] for row in grid]
    for cells in components:
        points = set(cells)
        top, left = min(r for r, _ in points), min(c for _, c in points)
        bottom, right = max(r for r, _ in points), max(c for _, c in points)
        for row0 in range(bottom - 2, top + 1):
            for col0 in range(right - 2, left + 1):
                local = {(r - row0, c - col0) for r, c in points}
                if not local or not local <= plus:
                    continue
                positions = [
                    (row0 + r, col0 + c)
                    for r, c in plus - local
                    if 0 <= row0 + r < height and 0 <= col0 + c < width
                ]
                if positions and all(grid[r][c] == marker for r, c in positions):
                    for r, c in positions:
                        output[r][c] = replacement
    return output
