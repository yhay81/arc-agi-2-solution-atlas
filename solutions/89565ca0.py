def components(grid, color):
    height, width = len(grid), len(grid[0])
    seen = set()
    result = []
    for r in range(height):
        for c in range(width):
            if grid[r][c] != color or (r, c) in seen:
                continue
            seen.add((r, c))
            todo = [(r, c)]
            points = []
            while todo:
                row, col = todo.pop()
                points.append((row, col))
                for rr, cc in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                    if (
                        0 <= rr < height
                        and 0 <= cc < width
                        and grid[rr][cc] == color
                        and (rr, cc) not in seen
                    ):
                        seen.add((rr, cc))
                        todo.append((rr, cc))
            result.append(points)
    return result


def hole_count(mask):
    height, width = len(mask), len(mask[0])
    open_cells = {(r, c) for r in range(height) for c in range(width) if not mask[r][c]}
    todo = []
    for r, c in tuple(open_cells):
        if r in (0, height - 1) or c in (0, width - 1):
            open_cells.remove((r, c))
            todo.append((r, c))
    while todo:
        r, c = todo.pop()
        for rr, cc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if (rr, cc) in open_cells:
                open_cells.remove((rr, cc))
                todo.append((rr, cc))
    count = 0
    while open_cells:
        count += 1
        start = open_cells.pop()
        todo = [start]
        while todo:
            r, c = todo.pop()
            for rr, cc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if (rr, cc) in open_cells:
                    open_cells.remove((rr, cc))
                    todo.append((rr, cc))
    return count


def solve(grid):
    a = grid
    height, width = len(a), len(a[0])
    colors = {value for row in a for value in row} - {0}
    noise = max(colors, key=lambda color: len(components(a, color)))
    counts = []
    for color in colors - {noise}:
        points = [(r, c) for r in range(height) for c in range(width) if a[r][c] == color]
        top = min(r for r, _ in points)
        left = min(c for _, c in points)
        bottom = max(r for r, _ in points)
        right = max(c for _, c in points)
        patch = [list(row[left : right + 1]) for row in a[top : bottom + 1]]
        ph, pw = len(patch), len(patch[0])
        mask = [[value == color for value in row] for row in patch]
        mask[0] = [True] * pw
        mask[-1] = [True] * pw
        for row in mask:
            row[0] = row[-1] = True
        for axis in (0, 1):
            rows = patch if axis == 0 else [list(row) for row in zip(*patch)]
            view = mask if axis == 0 else [list(row) for row in zip(*mask)]
            for y, row in enumerate(rows):
                groups = []
                for x, value in enumerate(row):
                    if value in (color, noise):
                        if groups and x == groups[-1][-1] + 1:
                            groups[-1].append(x)
                        else:
                            groups.append([x])
                for group in groups:
                    hits = [x for x in group if row[x] == color]
                    if len(hits) >= 2:
                        for x in range(min(hits), max(hits) + 1):
                            view[y][x] = True
            if axis == 1:
                mask = [list(row) for row in zip(*view)]
        old = [row[:] for row in mask]
        for y in range(ph):
            for x in range(pw):
                if (
                    patch[y][x] != 0
                    and not mask[y][x]
                    and (
                        (0 < y < ph - 1 and old[y - 1][x] and old[y + 1][x])
                        or (0 < x < pw - 1 and old[y][x - 1] and old[y][x + 1])
                    )
                ):
                    mask[y][x] = True
        counts.append((hole_count(mask), int(color)))
    counts.sort()
    output_width = max(count for count, _ in counts)
    return [[color if x < count else noise for x in range(output_width)] for count, color in counts]
