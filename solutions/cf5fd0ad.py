def rotate(grid):
    return [list(row) for row in zip(*grid)][::-1]


def hcat(*grids):
    return [sum((row[:] for row in rows), []) for rows in zip(*grids)]


def vcat(*grids):
    output = []
    for grid in grids:
        output.extend(grid)
    return output


def solve(grid):
    if len(grid) != len(grid[0]):
        return [row[:] for row in grid]
    r180 = rotate(rotate(grid))
    r270 = rotate(r180)
    r90 = rotate(grid)
    top = hcat(r180, r180, r270, r270)
    bottom = hcat(r90, r90, grid, grid)
    return vcat(top, top, bottom, bottom)
