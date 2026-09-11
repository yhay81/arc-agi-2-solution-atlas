def solve(grid):
    a = grid
    a = [row[:] for row in a]
    frames = []
    for r in range(len(a) - 4):
        for c in range(len(a[0]) - 4):
            block = [row[c : c + 5] for row in a[r : r + 5]]
            color = block[0][0]
            if (
                color
                and all(value == color for value in block[0])
                and all(value == color for value in block[-1])
                and all(row[0] == color for row in block)
                and all(row[-1] == color for row in block)
            ):
                frames.append((r, c, color, [row[1:-1] for row in block[1:-1]]))
    templates = {}
    for r, c, color, inside in frames:
        if any(value for row in inside for value in row):
            templates[color] = inside
    out = [row[:] for row in a]
    for r, c, color, inside in frames:
        if not any(value for row in inside for value in row) and color in templates:
            for i, row in enumerate(templates[color]):
                out[r + 1 + i][c + 1 : c + 4] = row
    return out
