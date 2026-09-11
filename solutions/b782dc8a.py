from collections import Counter


def solve(grid):
    h, w = len(grid), len(grid[0])
    counts = Counter(value for row in grid for value in row)
    values = sorted(counts)
    frequent = [value for value, _ in sorted(counts.items(), key=lambda item: -item[1])]
    if 0 not in frequent or len(frequent) < 3:
        return [row[:] for row in grid]
    fill_color = 0
    base_colours = set(frequent[:2])
    seed_colours = [int(value) for value in values if int(value) not in base_colours]
    if len(seed_colours) < 2:
        return [row[:] for row in grid]
    seed_counts = {
        colour: sum(value == colour for row in grid for value in row) for colour in seed_colours
    }
    center_colour = min(seed_colours, key=lambda colour: seed_counts[colour])
    arm_colour = max(seed_colours, key=lambda colour: seed_counts[colour])
    center_positions = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == center_colour]
    if len(center_positions) != 1:
        return [row[:] for row in grid]
    center_row, center_col = center_positions[0]
    seed_mask = {
        (r, c) for r in range(h) for c in range(w) if grid[r][c] in (center_colour, arm_colour)
    }
    remaining = {(r, c) for r in range(h) for c in range(w) if grid[r][c] == fill_color}
    selected = set()
    while remaining:
        start = remaining.pop()
        stack = [start]
        component = {start}
        while stack:
            row, col = stack.pop()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                cell = (row + dr, col + dc)
                if cell in remaining:
                    remaining.remove(cell)
                    stack.append(cell)
                    component.add(cell)
        if any(
            (
                0 <= row + dr < h and 0 <= col + dc < w and (row + dr, col + dc) in seed_mask
                for row, col in component
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1))
            )
        ):
            selected.update(component)
    output = [row[:] for row in grid]
    for row, col in selected:
        distance = abs(row - center_row) + abs(col - center_col)
        output[row][col] = center_colour if distance % 2 == 0 else arm_colour
    return output
