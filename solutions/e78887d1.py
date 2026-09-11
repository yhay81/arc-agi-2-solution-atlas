def solve(grid):
    g = grid
    start = max((r for r, row in enumerate(g) if any(row))) - 2
    blocks = [[row[c : c + 3] for row in g[start : start + 3]] for c in range(0, len(g[0]), 4)]
    colors = [next(v for row in p for v in row if v) for p in blocks]
    out = []
    for r in range(3):
        row = []
        for j, color in enumerate(colors):
            row.extend([color if v else 0 for v in blocks[(j + 1) % len(blocks)][r]] + [0])
        out.append(row[:-1])
    return out
