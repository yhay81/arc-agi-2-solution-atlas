def solve(grid):
    output = [[value if value in (6, 7) else 7 for value in row] for row in grid]
    unseen = {(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == 6}
    while unseen:
        pending = [unseen.pop()]
        component = []
        markers = set()
        while pending:
            r, c = pending.pop()
            component.append((r, c))
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])):
                    continue
                if (nr, nc) in unseen:
                    unseen.remove((nr, nc))
                    pending.append((nr, nc))
                elif grid[nr][nc] not in (6, 7):
                    markers.add(grid[nr][nc])
        if len(markers) == 1:
            color = markers.pop()
            for r, c in component:
                output[r][c] = color
    return output
