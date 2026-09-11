def solve(grid):
    a = grid
    b = [list(row) for row in zip(*a)][::-1]
    w = len(b[0])
    edge = [7] + [1] * w + [7]
    content = [[1] + row + [1] for row in b]
    return [edge[:]] + content + [edge[:]] + [row[:] for row in content] + [edge[:]]
