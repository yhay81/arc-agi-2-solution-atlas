def solve(grid):
    height, width = len(grid), len(grid[0])
    remaining = {(r, c) for r in range(height) for c in range(width) if grid[r][c]}
    counts = {}
    while remaining:
        start = remaining.pop()
        color = grid[start[0]][start[1]]
        stack = [start]
        while stack:
            r, c = stack.pop()
            for point in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if point in remaining:
                    remaining.remove(point)
                    stack.append(point)
        counts[color] = counts.get(color, 0) + 1
    if not counts:
        return [row[:] for row in grid]
    ordered = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    output_width = max(counts.values())
    return [
        [color if col >= output_width - count else 0 for col in range(output_width)]
        for color, count in ordered
    ]
