from collections import Counter


def solve(grid):
    height, width = len(grid), len(grid[0])
    bounds = []
    boundary_colors = []
    for lines in (grid, [[grid[r][c] for r in range(height)] for c in range(width)]):
        ranked = []
        for index, line in enumerate(lines):
            nonzero = [value for value in line if value]
            if not len(nonzero):
                ranked.append((0, index, 0))
                continue
            counts = Counter(nonzero)
            mode = next(value for value in counts if counts[value] == max(counts.values()))
            ranked.append((counts[mode], index, mode))
        ranked.sort(reverse=True)
        selected = sorted(ranked[:2], key=lambda item: item[1])
        if len(selected) != 2 or ranked[1][0] * 3 < len(lines[0]) * 2:
            return [row[:] for row in grid]
        bounds.append((selected[0][1], selected[1][1]))
        boundary_colors.append((selected[0][2], selected[1][2]))
    (top, bottom), (left, right) = bounds
    output = [row[left : right + 1] for row in grid[top : bottom + 1]]
    sides = (
        ("top", boundary_colors[0][0], 0),
        ("bottom", boundary_colors[0][1], len(output) - 1),
        ("left", boundary_colors[1][0], 0),
        ("right", boundary_colors[1][1], len(output[0]) - 1),
    )
    repeated: list[tuple[int, str, int]] = []
    for side, color, index in sides:
        mask = [[value == color for value in row] for row in output]
        if side in {"top", "bottom"}:
            mask[index] = [False] * len(mask[index])
        else:
            for row in mask:
                row[index] = False
        repeated.append((sum(sum(row) for row in mask), side, color))
    repeated.sort(reverse=True)
    if not repeated[0][0] or repeated[0][0] == repeated[1][0]:
        return [row[:] for row in grid]
    _, side, color = repeated[0]
    for row in range(len(output)):
        for col in range(len(output[0])):
            if output[row][col] != color:
                continue
            if side == "top":
                for r in range(row + 1):
                    output[r][col] = color
            elif side == "bottom":
                for r in range(row, len(output)):
                    output[r][col] = color
            elif side == "left":
                output[row][: col + 1] = [color] * (col + 1)
            else:
                output[row][col:] = [color] * (len(output[0]) - col)
    return output
