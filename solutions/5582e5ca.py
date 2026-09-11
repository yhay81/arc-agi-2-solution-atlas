from collections import Counter


def solve(grid):
    counts = Counter(value for row in grid for value in row)
    color = min(counts, key=lambda value: (-counts[value], value))
    return [[color] * len(grid[0]) for _ in grid]
