def solve(grid):
    key = [[grid[r][c] != 0 for c in range(1, 4)] for r in range(1, 4)]
    if sum(key[0]) == 3:
        color = 1
    else:
        color = 2 if key[0][0] else 3
    return [[color if grid[r][c] else 0 for c in range(5, 8)] for r in range(1, 4)]
