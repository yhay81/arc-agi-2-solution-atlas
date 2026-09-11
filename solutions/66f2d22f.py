def solve(grid):
    g = grid
    h, w = (len(g), len(g[0]))
    half = w // 2
    if w % 2:
        raise ValueError("Expected equal horizontal halves")
    return [[5 if g[r][c] == g[r][c + half] == 0 else 0 for c in range(half)] for r in range(h)]
