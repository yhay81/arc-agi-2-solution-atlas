def _components(grid):
    unseen = {(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value}
    groups = []
    while unseen:
        pending = [unseen.pop()]
        group = []
        while pending:
            r, c = pending.pop()
            group.append((r, c))
            for point in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if point in unseen and grid[point[0]][point[1]] == grid[r][c]:
                    unseen.remove(point)
                    pending.append(point)
        groups.append(group)
    return groups


def solve(grid):
    groups = _components(grid)
    rectangles = [group for group in groups if len(group) >= 4]
    output = [row[:] for row in grid]
    for noise in (group for group in groups if len(group) < 4):
        replacement = 0
        neighbors = {
            (r + dr, c + dc) for r, c in noise for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1))
        }
        for rectangle in rectangles:
            if len(neighbors.intersection(rectangle)) >= 2:
                r, c = rectangle[0]
                replacement = grid[r][c]
                break
        for r, c in noise:
            output[r][c] = replacement
    return output
