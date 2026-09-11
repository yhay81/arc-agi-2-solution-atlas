def _negative_photo_pair(grid):
    positions = [(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value != 0]
    if not len(positions):
        return [row[:] for row in grid]
    negative = [[8 if value == 0 else 0 for value in reversed(row)] for row in grid]
    width = len(grid[0])
    right = 2 * sum(c for _, c in positions) >= len(positions) * (width - 1)
    return [((row + neg) if right else (neg + row)) for row, neg in zip(grid, negative)]


def solve(grid):
    return _negative_photo_pair(grid)
