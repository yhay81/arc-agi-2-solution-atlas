def solve(grid):
    source = [[v != 0 for v in row] for row in grid]
    output = [[0] * len(grid[0]) for _ in range(3)]
    for col in range(0, len(source[0]), 3):
        glyph = [row[col : col + 3] for row in source]
        size = sum(sum(row) for row in glyph)
        if size == 1:
            color = 4
        elif size == 8:
            color = 3
        elif all(sum(row) == 1 for row in glyph):
            color = 9
        else:
            color = 6 if any(glyph[0]) else 1
        for r in range(3):
            output[r][col : col + 3] = [color] * 3
    return output
