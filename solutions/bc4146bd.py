def solve(grid):
    a = grid
    mirror = [row[::-1] for row in a]
    return [row + rev + row + rev + row for row, rev in zip(a, mirror)]
