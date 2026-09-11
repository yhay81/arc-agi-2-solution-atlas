from collections import Counter


def solve(grid):
    a = [list(map(int, row)) for row in grid]
    bg = Counter(value for row in a for value in row).most_common(1)[0][0]
    bars = [
        col for col in range(len(a[0])) if len({row[col] for row in a}) == 1 and a[0][col] != bg
    ]
    width = min(bars) if bars else len(a[0])
    panel = [row[:width] for row in a]
    fg = Counter(value for row in panel for value in row if value != bg).most_common(1)[0][0]
    height = len(panel)
    mask = [[panel[row][col] == fg for col in range(width)] for row in range(height)]
    seen = set()
    objects = []
    for row in range(height):
        for col in range(width):
            if not mask[row][col] or (row, col) in seen:
                continue
            stack = [(row, col)]
            seen.add((row, col))
            component = []
            while stack:
                current_row, current_col = stack.pop()
                component.append((current_row, current_col))
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        point = (current_row + dr, current_col + dc)
                        if (
                            (dr or dc)
                            and 0 <= point[0] < height
                            and 0 <= point[1] < width
                            and mask[point[0]][point[1]]
                            and point not in seen
                        ):
                            seen.add(point)
                            stack.append(point)
            objects.append(component)
    shape = max(objects, key=len)
    dots = {component[0] for component in objects if len(component) == 1}
    shape_cells = set(shape)
    candidates = []
    for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        extreme = max(row * dr + col * dc for row, col in shape_cells)
        heads = [point for point in shape_cells if point[0] * dr + point[1] * dc == extreme]
        if len(heads) != 1:
            continue
        head = heads[0]
        perp = (-dc, dr)
        if all(
            (
                head[0]
                + (row - head[0]) * dr * dr
                + (col - head[1]) * dc * dr
                - ((row - head[0]) * perp[0] + (col - head[1]) * perp[1]) * perp[0],
                head[1]
                + (row - head[0]) * dr * dc
                + (col - head[1]) * dc * dc
                - ((row - head[0]) * perp[0] + (col - head[1]) * perp[1]) * perp[1],
            )
            in shape_cells
            for row, col in shape_cells
        ):
            candidates.append((head, (dr, dc)))
    pos, direction = candidates[0]
    origin, initial = pos, direction
    while dots:
        options = []
        for point in dots:
            dy, dx = point[0] - pos[0], point[1] - pos[1]
            if (dy == 0) != (dx == 0):
                step = ((dy > 0) - (dy < 0), (dx > 0) - (dx < 0))
                if step != (-direction[0], -direction[1]):
                    options.append((abs(dy) + abs(dx), point, step))
        _, pos, direction = min(options)
        dots.remove(pos)
    directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
    turns = (directions.index(direction) - directions.index(initial)) % 4
    output = [[bg] * width for _ in range(height)]
    for row, col in shape_cells:
        y, x = row - origin[0], col - origin[1]
        for _ in range(turns):
            y, x = x, -y
        target_row, target_col = pos[0] + y, pos[1] + x
        if 0 <= target_row < height and 0 <= target_col < width:
            output[target_row][target_col] = fg
    return output
