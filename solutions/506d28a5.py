def solve(grid):
    g = grid
    half = len(g) // 2
    return [[3 if a or b else 0 for a, b in zip(ar, br)] for ar, br in zip(g[:half], g[half + 1 :])]
