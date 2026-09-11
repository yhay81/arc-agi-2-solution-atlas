from collections import Counter
from math import ceil, floor


def solve(grid):
    a = [[int(value) for value in row] for row in grid]
    values = [value for row in a for value in row]
    bg = Counter(values).most_common(1)[0][0]
    non_background = [value for value in values if value != bg]
    wall = Counter(non_background).most_common(1)[0][0]
    wall_cells = [
        (row, col) for row, line in enumerate(a) for col, value in enumerate(line) if value == wall
    ]
    top = min(row for row, _ in wall_cells)
    left = min(col for _, col in wall_cells)
    bottom = max(row for row, _ in wall_cells)
    right = max(col for _, col in wall_cells)
    patch_values = [
        a[row][col]
        for row in range(top, bottom + 1)
        for col in range(left, right + 1)
        if a[row][col] not in (bg, wall)
    ]
    fc = Counter(patch_values).most_common(1)[0][0]
    seed = [
        sum(row for row, line in enumerate(a) for col, value in enumerate(line) if value == fc)
        / sum(value == fc for line in a for value in line),
        sum(col for line in a for col, value in enumerate(line) if value == fc)
        / sum(value == fc for line in a for value in line),
    ]
    center = [(top + bottom) / 2, (left + right) / 2]
    delta = [seed[0] - center[0], seed[1] - center[1]]
    axis = max(range(2), key=lambda index: abs(delta[index]))
    sign = -int((delta[axis] > 0) - (delta[axis] < 0))
    rot = {(0, 1): 0, (0, -1): 2, (1, -1): 1, (1, 1): 3}[axis, sign]
    for _ in range(rot):
        a = [list(column) for column in zip(*a)][::-1]
    output = [row[:] for row in a]
    height, width = len(a), len(a[0])
    wall_cells = [
        (row, col) for row, line in enumerate(a) for col, value in enumerate(line) if value == wall
    ]
    top = min(row for row, _ in wall_cells)
    left = min(col for _, col in wall_cells)
    bottom = max(row for row, _ in wall_cells)
    right = max(col for _, col in wall_cells)
    bounds_by_row = {}
    for row in range(top, bottom + 1):
        columns = [col for col, value in enumerate(a[row]) if value == wall]
        if columns:
            bounds_by_row[row] = (min(columns), max(columns))
    last = bounds_by_row[bottom]
    previous = bounds_by_row[bottom - 2]
    slope = abs(last[0] - previous[0]) / 2
    left_edge, right_edge = last
    if left_edge == right_edge:
        full_rows = [row for row, bounds in bounds_by_row.items() if bounds[0] != bounds[1]]
        row = max(full_rows)
        low, high = bounds_by_row[row]
        midpoint = (low + high) / 2
        if left_edge < midpoint:
            right_edge = high + slope * (bottom - row)
        else:
            left_edge = low - slope * (bottom - row)
    blocked = set()
    for row in range(top + 1, height):
        if row <= bottom:
            low, high = bounds_by_row.get(row, (left_edge, right_edge))
            if low == high:
                if low < (left_edge + right_edge) / 2:
                    high = right_edge
                else:
                    low = left_edge
            low += 1
            high -= 1
        else:
            expansion = floor((row - bottom - 1) * slope + 1e-9)
            low = left_edge - expansion
            high = right_edge + expansion
        for col in range(max(0, ceil(low)), min(width - 1, floor(high)) + 1):
            if a[row][col] not in (bg, wall, fc):
                blocked.add(col)
            if col not in blocked and a[row][col] in (bg, fc):
                output[row][col] = fc
    for _ in range((4 - rot) % 4):
        output = [list(column) for column in zip(*output)][::-1]
    return output
