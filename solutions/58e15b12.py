def components(grid, color):
    h, w = len(grid), len(grid[0])
    seen, result = set(), []
    for r in range(h):
        for c in range(w):
            if grid[r][c] != color or (r, c) in seen:
                continue
            seen.add((r, c))
            stack = [(r, c)]
            part = []
            while stack:
                x, y = stack.pop()
                part.append((x, y))
                for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    if (
                        0 <= nx < h
                        and 0 <= ny < w
                        and grid[nx][ny] == color
                        and (nx, ny) not in seen
                    ):
                        seen.add((nx, ny))
                        stack.append((nx, ny))
            result.append(part)
    return result


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    out = [row[:] for row in a]
    h, w = len(a), len(a[0])
    for color in set(v for row in a for v in row) - {0}:
        objs = sorted(components(a, color), key=lambda ps: min(c for _, c in ps))
        if not (len(objs) == 2):
            raise ValueError("task assumptions are not satisfied")
        for i, ps in enumerate(objs):
            height = max(r for r, _ in ps) - min(r for r, _ in ps) + 1
            side = -1 if i == 0 else 1
            for direction in (-1, 1):
                for n in range(1, max(h, w)):
                    for r, c in ps:
                        y, x = (r + direction * n * height, c + side * n)
                        if 0 <= y < h and 0 <= x < w:
                            out[y][x] = color if out[y][x] in (0, color) else 6
    return out
