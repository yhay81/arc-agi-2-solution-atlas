from collections import Counter


def _kronecker_most_frequent_color(grid):
    counts = Counter(v for row in grid for v in row if v)
    if not counts:
        return [row[:] for row in grid]
    color = counts.most_common(1)[0][0]
    h, w = len(grid), len(grid[0])
    return [
        [grid[ir][ic] if grid[r][c] == color else 0 for c in range(w) for ic in range(w)]
        for r in range(h)
        for ir in range(h)
    ]


def solve(grid):
    return _kronecker_most_frequent_color(grid)
