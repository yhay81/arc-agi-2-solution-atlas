from collections import Counter


def solve(grid):
    g = grid
    n = next((c for c, v in enumerate(g[0]) if v == 5))
    stride = n + 1
    templates = {}
    mapping = {}
    macro = [[0] * n for _ in range(n)]
    for col in range(0, len(g[0]), stride):
        if col + n > len(g[0]):
            break
        tile = [row[col : col + n] for row in g[:n]]
        colors = [v for row in tile for v in row if v not in (0, 5)]
        if not colors:
            continue
        co = Counter(colors).most_common(1)[0][0]
        templates[co] = tile
        palette = {
            g[r][c]
            for r in range(2 * stride, len(g))
            for c in range(col, col + n)
            if g[r][c] not in (0, 5)
        }
        if len(palette) != 1:
            raise ValueError("color-replacement legend is not unique")
        mapping[co] = next(iter(palette))
        for r in range(n):
            for c in range(n):
                v = g[stride + r][col + c]
                if v:
                    if macro[r][c] and macro[r][c] != v:
                        raise ValueError("instruction shapes to combine overlap")
                    macro[r][c] = v
    out = [[0] * (n * n) for _ in range(n * n)]
    for r in range(n * n):
        for c in range(n * n):
            co = macro[r // n][c // n]
            if co and templates[co][r % n][c % n]:
                out[r][c] = mapping[co]
    return out
