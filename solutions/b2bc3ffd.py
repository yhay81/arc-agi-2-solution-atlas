def colored_components(a, excluded):
    seen = set()
    for color in sorted({value for row in a for value in row} - set(excluded)):
        for r, row in enumerate(a):
            for c, value in enumerate(row):
                if value != color or (r, c) in seen:
                    continue
                stack = [(r, c)]
                seen.add((r, c))
                points = []
                while stack:
                    x, y = stack.pop()
                    points.append((x, y))
                    for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                        if (
                            0 <= nx < len(a)
                            and 0 <= ny < len(a[0])
                            and a[nx][ny] == color
                            and (nx, ny) not in seen
                        ):
                            seen.add((nx, ny))
                            stack.append((nx, ny))
                yield color, points


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    objects = list(colored_components(a, (7, 8)))
    out = [row[:] for row in a]
    for color, points in objects:
        for r, c in points:
            out[r][c] = 7
    for color, points in objects:
        destination = [(r - len(points), c) for r, c in points]
        if any(r < 0 for r, _ in destination):
            raise ValueError("Object jumps out of the grid")
        if any(out[r][c] != 7 for r, c in destination):
            raise ValueError("Jump collides with another object")
        for r, c in destination:
            out[r][c] = color
    return out
