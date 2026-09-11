def solve(grid):
    colors = {v for row in grid for v in row} - {0}
    counts = {color: sum(row.count(color) for row in grid) for color in colors}
    candidates = [color for color, count in counts.items() if count == max(counts.values())]
    if len(candidates) != 1:
        raise ValueError("Expected one most frequent nonblack object color")
    color = candidates[0]
    out = [row[:] for row in grid]
    width = len(grid[0])
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value == color:
                out[r][width - c - 1] = color
    return out
