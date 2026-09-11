from collections import Counter


def solve(grid):
    height, width = len(grid), len(grid[0])
    inside = Counter(value for row in grid[1:-1] for value in row[1:-1])
    background, figure = [value for value, _ in inside.most_common(2)]
    direction_color = {
        (-1, 0): grid[0][1],
        (1, 0): grid[-1][1],
        (0, -1): grid[1][0],
        (0, 1): grid[1][-1],
    }
    output = [row[:] for row in grid]
    for r in range(1, height - 1):
        for c in range(1, width - 1):
            if grid[r][c] != background:
                continue
            open_sides = [
                direction
                for direction in direction_color
                if grid[r + direction[0]][c + direction[1]] == background
            ]
            solid_sides = sum(grid[r + dr][c + dc] == figure for dr, dc in direction_color)
            if len(open_sides) == 1 and solid_sides == 3:
                dr, dc = open_sides[0]
                center = (r + dr, c + dc)
                color = direction_color[(dr, dc)]
                for rr, cc in (
                    center,
                    (center[0] - 1, center[1]),
                    (center[0] + 1, center[1]),
                    (center[0], center[1] - 1),
                    (center[0], center[1] + 1),
                ):
                    output[rr][cc] = color
    return output
