from collections import Counter
from statistics import median


def solve(grid):
    height, width = len(grid), len(grid[0])
    seen = set()
    objects = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] in (0, 5) or (row, col) in seen:
                continue
            stack = [(row, col)]
            seen.add((row, col))
            cells = []
            while stack:
                current_row, current_col = stack.pop()
                cells.append((current_row, current_col))
                for row_step in (-1, 0, 1):
                    for col_step in (-1, 0, 1):
                        next_row = current_row + row_step
                        next_col = current_col + col_step
                        if (
                            0 <= next_row < height
                            and 0 <= next_col < width
                            and grid[next_row][next_col] not in (0, 5)
                            and (next_row, next_col) not in seen
                        ):
                            seen.add((next_row, next_col))
                            stack.append((next_row, next_col))
            top = min(row for row, _ in cells)
            left = min(col for _, col in cells)
            bottom = max(row for row, _ in cells)
            right = max(col for _, col in cells)
            patch = [line[left : right + 1] for line in grid[top : bottom + 1]]
            objects.append((top, left, bottom, right, patch))

    marker = [(row, col) for row in range(height) for col in range(width) if grid[row][col] == 5]
    top = min(row for row, _ in marker)
    left = min(col for _, col in marker)
    bottom = max(row for row, _ in marker)
    right = max(col for _, col in marker)
    output = [[0] * (right - left + 1) for _ in range(bottom - top + 1)]
    centers = [((item[0] + item[2]) / 2, (item[1] + item[3]) / 2) for item in objects]
    axis = max(
        range(2),
        key=lambda index: (
            max(point[index] for point in centers) - min(point[index] for point in centers)
        ),
    )
    target = ((top + bottom) / 2, (left + right) / 2)
    direction = 1 if target[axis] > sum(point[axis] for point in centers) / len(centers) else -1
    objects.sort(
        key=lambda item: (
            direction * ((item[0] + item[2]) / 2 if axis == 0 else (item[1] + item[3]) / 2)
        )
    )
    patches = [item[4] for item in objects]
    colors = [
        Counter(cell for line in patch for cell in line if cell).most_common(1)[0][0]
        for patch in patches
    ]
    period = next(
        (
            size
            for size in range(1, len(colors) + 1)
            if all(colors[index] == colors[index % size] for index in range(len(colors)))
        ),
        len(colors),
    )
    color_at = lambda index: colors[index % period]

    if axis == 1 and all(
        len({cell for line in patch for cell in line if cell}) == 1 for patch in patches
    ):
        widths = [len(patch[0]) for patch in patches]
        if len(set(widths)) == 1:
            stride = objects[1][1] - objects[0][1]
            step = (left - objects[0][1]) // stride
            patch_height = len(patches[0]) + step * (len(patches[1]) - len(patches[0]))
            fill_color = color_at(step)
            start = objects[0][0]
            for row in range(len(output)):
                for col in range(len(output[0])):
                    delta_row = top + row - start
                    delta_col = left + col - (objects[0][1] + step * stride)
                    if (
                        0 <= delta_row < patch_height
                        and 0 <= delta_col < widths[0]
                        and (delta_col in (0, widths[0] - 1) or delta_row % 2 == 0)
                    ):
                        output[row][col] = fill_color
        else:
            step = len(objects)
            start_col = objects[-1][3] + 2
            next_width = widths[-1] + widths[-1] - widths[-2]
            end_row = objects[-1][2]
            next_height = len(patches[-1]) + len(patches[-1]) - len(patches[-2])
            fill_color = color_at(step)
            for row in range(len(output)):
                for col in range(len(output[0])):
                    absolute_row, absolute_col = top + row, left + col
                    if (
                        end_row - next_height < absolute_row <= end_row
                        and start_col <= absolute_col < start_col + next_width
                        and (absolute_col == start_col or absolute_row in (end_row, end_row - 2))
                    ):
                        output[row][col] = fill_color
    elif axis == 1 and all(len(patch[0]) == 2 for patch in patches):
        center = int(median((item[0] + item[2]) / 2 for item in objects))
        base = patches[-1]
        middle = len(base) // 2
        cycle = []
        for offset in range(0, middle, 2):
            value = base[middle + offset][0]
            if value in cycle:
                break
            cycle.append(value)
        for row in range(len(output)):
            distance = abs(top + row - center)
            step = distance // 2
            old = cycle[step % len(cycle)]
            new = cycle[(step + 1) % len(cycle)]
            output[row] = (
                [old, old] if distance % 2 == 0 else ([new, old] if step % 2 == 0 else [old, new])
            )
        next_half = len(base) // 2 + 2
        for row in range(len(output)):
            if abs(top + row - center) == next_half:
                output[row][0 if len(objects) % 2 == 0 else 1] = 0
    elif axis == 0 and all(len(patch) == 3 for patch in patches):
        fill_color = color_at(len(objects))
        same = [
            item
            for item in objects
            if Counter(cell for line in item[4] for cell in line if cell).most_common(1)[0][0]
            == fill_color
        ]
        source = max(same, key=lambda item: len(item[4][0]))
        patch = source[4]
        patch_width = len(patch[0])
        repeat = next(
            size
            for size in range(1, patch_width)
            if all(
                patch[row][col] == patch[row][col - size]
                for row in range(3)
                for col in range(size, patch_width)
            )
        )
        stride = objects[-1][0] - objects[-2][0]
        start = objects[-1][0] + stride
        for row in range(len(output)):
            offset = top + row - start
            if 0 <= offset < 3:
                for col in range(len(output[0])):
                    output[row][col] = patch[offset][(left + col - source[1]) % repeat]
    else:
        layers = len(patches[-1]) // 2 + 1
        output_width = 4 * layers + 1
        first_row_colors = [next(cell for cell in patch[0] if cell) for patch in patches]
        top_color = first_row_colors[len(objects) % 2]
        other_color = next(value for value in first_row_colors if value != top_color)
        for layer in range(layers):
            fill_color = top_color if layer % 2 == 0 else other_color
            previous = other_color if layer % 2 == 0 else top_color
            row = 2 * layer
            margin = 2 * (layers - 1 - layer)
            end = output_width - 1 - margin
            if layer == 0:
                output[row][margin : end + 1] = [fill_color] * (end - margin + 1)
            else:
                output[row][margin : margin + 3] = [fill_color] * 3
                output[row][end - 2 : end + 1] = [fill_color] * 3
            output[row + 1][margin] = fill_color
            output[row + 1][end] = fill_color
            if layer:
                output[row + 1][margin + 2] = previous
                output[row + 1][end - 2] = previous
    return output
