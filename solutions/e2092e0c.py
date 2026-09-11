def solve(grid):
    source = [list(map(int, row)) for row in grid]
    if len(source) < 5 or len(source[0]) < 5:
        return [row[:] for row in source]
    height, width = len(source), len(source[0])
    seen = set()
    key_component = None
    for row in range(height):
        for col in range(width):
            if source[row][col] != 5 or (row, col) in seen:
                continue
            stack = [(row, col)]
            seen.add((row, col))
            component = []
            while stack:
                current_row, current_col = stack.pop()
                component.append((current_row, current_col))
                for next_row, next_col in (
                    (current_row - 1, current_col),
                    (current_row + 1, current_col),
                    (current_row, current_col - 1),
                    (current_row, current_col + 1),
                ):
                    if (
                        0 <= next_row < height
                        and 0 <= next_col < width
                        and source[next_row][next_col] == 5
                        and (next_row, next_col) not in seen
                    ):
                        seen.add((next_row, next_col))
                        stack.append((next_row, next_col))
            if len(component) != 7:
                continue
            rows = [r for r, _ in component]
            cols = [c for _, c in component]
            top, bottom, left, right = min(rows), max(rows), min(cols), max(cols)
            expected = {
                *((bottom, col) for col in range(left, right + 1)),
                *((row, right) for row in range(top, bottom)),
            }
            if (bottom - top, right - left) == (3, 3) and set(component) == expected:
                key_component = component
                break
        if key_component is not None:
            break
    if key_component is None:
        return [row[:] for row in source]
    top = min(row for row, _ in key_component)
    left = min(col for _, col in key_component)
    key = [row[left : left + 3] for row in source[top : top + 3]]
    matches = []
    for target_top in range(height - 4):
        for target_left in range(width - 4):
            if all(
                source[target_top + row + 1][target_left + col + 1] == key[row][col]
                for row in range(3)
                for col in range(3)
            ):
                matches.append((target_top, target_left))
    if len(matches) != 1:
        return [row[:] for row in source]
    target_top, target_left = matches[0]
    output = [row[:] for row in source]
    for offset in range(5):
        output[target_top][target_left + offset] = 5
        output[target_top + 4][target_left + offset] = 5
        output[target_top + offset][target_left] = 5
        output[target_top + offset][target_left + 4] = 5
    return output
