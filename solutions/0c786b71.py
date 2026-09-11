def _reverse_mirror_quad(grid):
    top = [row[::-1] for row in grid[::-1]] + [row[:] for row in grid[::-1]]
    bottom = [row[::-1] for row in grid] + [row[:] for row in grid]
    return [
        a + b for a, b in zip([row[::-1] for row in grid[::-1]], [row[:] for row in grid[::-1]])
    ] + [a + b for a, b in zip([row[::-1] for row in grid], [row[:] for row in grid])]


def solve(grid):
    return _reverse_mirror_quad(grid)
