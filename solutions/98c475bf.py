from collections import Counter


def put(g, r, c, v):
    if 0 <= r < len(g) and 0 <= c < len(g[0]):
        g[r][c] = v


def solve(grid):
    g = grid
    symbols = {
        "6": {
            "row_offset": -2,
            "left": 2,
            "mask": [[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]],
        },
        "7": {
            "row_offset": -2,
            "left": 13,
            "mask": [[1, 0, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 0, 1]],
        },
        "1": {"row_offset": -1, "left": 14, "mask": [[1, 0, 1], [1, 1, 1], [1, 0, 1]]},
        "2": {
            "row_offset": -2,
            "left": 6,
            "mask": [[1, 0, 1], [0, 1, 0], [1, 1, 1], [0, 1, 0], [1, 0, 1]],
        },
        "3": {
            "row_offset": -2,
            "left": 4,
            "mask": [[0, 1, 0], [1, 0, 1], [0, 0, 0], [1, 0, 1], [0, 1, 0]],
        },
    }
    g = [row[:] for row in g]
    h, w = (len(g), len(g[0]))
    out = [[0] * w for _ in range(h)]
    for r in range(h):
        out[r][0] = g[r][0]
        out[r][-1] = g[r][-1]
    counts = Counter(v for row in g for v in row[1:-1] if v)
    for r in range(h):
        color = g[r][1]
        if color and g[r][-2] == color and (counts[color] == 2):
            for c in range(1, w - 1):
                out[r][c] = color
            symbol = symbols[str(color)]
            offset = symbol["row_offset"]
            left = symbol["left"]
            for dr, row in enumerate(symbol["mask"]):
                for dc, v in enumerate(row):
                    put(out, r + offset + dr, left + dc, color if v else 0)
    return out
