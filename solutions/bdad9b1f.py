def _cross_lines(grid):
    eights = [(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == 8]
    twos = [(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == 2]
    if not len(eights) or not len(twos):
        return [row[:] for row in grid]
    col = max(range(len(grid[0])), key=lambda c: (sum(x == c for _, x in eights), -c))
    row = max(range(len(grid)), key=lambda r: (sum(x == r for x, _ in twos), -r))
    output = [[0] * len(grid[0]) for _ in grid]
    for r in range(len(grid)):
        output[r][col] = 8
    output[row] = [2] * len(grid[0])
    output[row][col] = 4
    return output


def solve(grid):
    return _cross_lines(grid)
