def solve(grid):
    height, width = len(grid), len(grid[0])
    background = 8
    seen = set()
    components = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] == background or (row, col) in seen:
                continue
            stack = [(row, col)]
            seen.add((row, col))
            cells = []
            while stack:
                r, c = stack.pop()
                cells.append((r, c))
                for rr, cc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if (
                        0 <= rr < height
                        and 0 <= cc < width
                        and grid[rr][cc] != background
                        and (rr, cc) not in seen
                    ):
                        seen.add((rr, cc))
                        stack.append((rr, cc))
            components.append(cells)
    seeds = []
    template = None
    bars = []
    for cells in components:
        if len(cells) == 1:
            seeds.append(cells[0])
            continue
        top, left = min(r for r, _ in cells), min(c for _, c in cells)
        bottom, right = max(r for r, _ in cells), max(c for _, c in cells)
        crop = [row[left : right + 1] for row in grid[top : bottom + 1]]
        coords = [[(r, c) for c in range(left, right + 1)] for r in range(top, bottom + 1)]
        if template is None:
            template = crop if len(crop) > len(crop[0]) else [list(col) for col in zip(*crop)]

        for flip in (False, True):
            values = [row[::-1] for row in crop] if flip else [row[:] for row in crop]
            points = [row[::-1] for row in coords] if flip else [row[:] for row in coords]
            for turns in range(4):
                transformed_values, transformed_points = values, points
                for _ in range(turns):
                    transformed_values = [list(row) for row in zip(*transformed_values[::-1])]
                    transformed_points = [list(row) for row in zip(*transformed_points[::-1])]
                if transformed_values != template:
                    continue
                origin = transformed_points[0][0]
                down = (
                    transformed_points[1][0][0] - origin[0],
                    transformed_points[1][0][1] - origin[1],
                )
                across = (
                    transformed_points[0][1][0] - origin[0],
                    transformed_points[0][1][1] - origin[1],
                )
                bars.append((len(transformed_values), origin, down, across))
    if not (bars):
        raise ValueError("task assumptions are not satisfied")
    choices = []
    for seed in seeds:
        candidates = []
        for length, origin, down, across in bars:
            delta = (seed[0] - origin[0], seed[1] - origin[1])
            r = delta[0] * down[0] + delta[1] * down[1]
            c = delta[0] * across[0] + delta[1] * across[1]
            on_normal = (seed[0] in (0, height - 1) and across[0] != 0) or (
                seed[1] in (0, width - 1) and across[1] != 0
            )
            if on_normal and 0 <= r < length and (c < 0 or c >= 2):
                candidates.append(
                    (min(abs(c), abs(c - 1)), r, 1 if c >= 2 else -1, grid[seed[0]][seed[1]])
                )
        if candidates:
            choices.append(min(candidates))
    if not (choices and len({choice[2] for choice in choices}) == 1):
        raise ValueError("task assumptions are not satisfied")
    side = choices[0][2]
    palette = {choice[1]: choice[3] for choice in choices}
    output = [row[:] for row in grid]
    for length, origin, down, across in bars:
        for row, color in palette.items():
            r = origin[0] + row * down[0] + (2 if side == 1 else -1) * across[0]
            c = origin[1] + row * down[1] + (2 if side == 1 else -1) * across[1]
            while (
                0 <= r < height and 0 <= c < width and (grid[r][c] == background or (r, c) in seeds)
            ):
                output[r][c] = color
                r += side * across[0]
                c += side * across[1]
    return output
