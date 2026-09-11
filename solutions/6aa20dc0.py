def solve(grid):
    height, width = len(grid), len(grid[0])
    values = {}
    for row in grid:
        for value in row:
            values[value] = values.get(value, 0) + 1
    background = max(values, key=values.get)
    windows = []
    for top in range(height - 2):
        for left in range(width - 2):
            motif = [row[left : left + 3] for row in grid[top : top + 3]]
            counts = {}
            for row in motif:
                for value in row:
                    if value != background:
                        counts[value] = counts.get(value, 0) + 1
            if (
                len(counts) == 3
                and sum(count == 1 for count in counts.values()) == 2
                and max(counts.values()) >= 2
            ):
                windows.append(
                    (
                        top,
                        left,
                        motif,
                        sorted(value for value, count in counts.items() if count == 1),
                    )
                )
    if len(windows) != 1:
        return [row[:] for row in grid]
    template_top, template_left, template, key_colors = windows[0]
    key_positions = {}
    for row in range(3):
        for col in range(3):
            if template[row][col] in key_colors and template[row][col] not in key_positions:
                key_positions[template[row][col]] = (row, col)
    remaining = [row[:] for row in grid]
    for row in range(template_top, template_top + 3):
        for col in range(template_left, template_left + 3):
            remaining[row][col] = background
    seen = set()
    blocks = []
    for row in range(height):
        for col in range(width):
            if remaining[row][col] == background or (row, col) in seen:
                continue
            color = remaining[row][col]
            stack = [(row, col)]
            seen.add((row, col))
            cells = []
            while stack:
                current_row, current_col = stack.pop()
                cells.append((current_row, current_col))
                for row_delta, col_delta in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    next_row = current_row + row_delta
                    next_col = current_col + col_delta
                    if (
                        0 <= next_row < height
                        and 0 <= next_col < width
                        and (next_row, next_col) not in seen
                        and remaining[next_row][next_col] == color
                    ):
                        seen.add((next_row, next_col))
                        stack.append((next_row, next_col))
            rows = [cell[0] for cell in cells]
            cols = [cell[1] for cell in cells]
            block_height = max(rows) - min(rows) + 1
            block_width = max(cols) - min(cols) + 1
            if (
                color in key_colors
                and block_height == block_width
                and len(cells) == block_height * block_width
            ):
                blocks.append((color, min(rows), min(cols), block_height))
    if not blocks:
        return [row[:] for row in grid]
    transforms = (
        (1, 0, 0, 1),
        (1, 0, 0, -1),
        (0, 1, -1, 0),
        (0, -1, -1, 0),
        (-1, 0, 0, -1),
        (-1, 0, 0, 1),
        (0, -1, 1, 0),
        (0, 1, 1, 0),
    )
    first_key, second_key = key_colors
    pairs = []
    for first in blocks:
        if first[0] != first_key:
            continue
        for second in blocks:
            if second[0] != second_key or second[3] != first[3]:
                continue
            scale = first[3]
            target_delta = (second[1] - first[1], second[2] - first[2])
            local_delta = (
                (key_positions[second_key][0] - key_positions[first_key][0]) * scale,
                (key_positions[second_key][1] - key_positions[first_key][1]) * scale,
            )
            for a, b, c, d in transforms:
                if (
                    a * local_delta[0] + b * local_delta[1],
                    c * local_delta[0] + d * local_delta[1],
                ) == target_delta:
                    pairs.append((first, (a, b, c, d)))
    if not pairs:
        return [row[:] for row in grid]
    output = [row[:] for row in grid]
    first_position = key_positions[first_key]
    for first, (a, b, c, d) in pairs:
        scale = first[3]
        for row in range(3):
            for col in range(3):
                if template[row][col] == background:
                    continue
                local_row = (row - first_position[0]) * scale
                local_col = (col - first_position[1]) * scale
                target_row = first[1] + a * local_row + b * local_col
                target_col = first[2] + c * local_row + d * local_col
                for row_delta in range(scale):
                    for col_delta in range(scale):
                        final_row = target_row + row_delta
                        final_col = target_col + col_delta
                        if (
                            0 <= final_row < height
                            and 0 <= final_col < width
                            and output[final_row][final_col] == background
                        ):
                            output[final_row][final_col] = template[row][col]
    return output
