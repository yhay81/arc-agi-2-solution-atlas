from collections import Counter


def solve(grid):
    if not grid or not grid[0]:
        return [row[:] for row in grid]
    height, width = len(grid), len(grid[0])
    values = sorted({value for row in grid for value in row})
    if not values:
        return [row[:] for row in grid]
    counts = Counter(value for row in grid for value in row)
    background = min(values, key=lambda value: (-counts[value], value))
    unseen = {
        (row, col) for row in range(height) for col in range(width) if grid[row][col] != background
    }
    components = []
    while unseen:
        start = unseen.pop()
        stack = [start]
        component = [start]
        while stack:
            row, col = stack.pop()
            for next_row, next_col in (
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1),
            ):
                cell = (next_row, next_col)
                if cell in unseen:
                    unseen.remove(cell)
                    stack.append(cell)
                    component.append(cell)
        components.append(component)
    if len(components) < 2:
        return [row[:] for row in grid]
    components.sort(key=len)
    template_cells = components[0]
    top = min(row for row, _ in template_cells)
    bottom = max(row for row, _ in template_cells)
    left = min(col for _, col in template_cells)
    right = max(col for _, col in template_cells)
    template = [row[left : right + 1] for row in grid[top : bottom + 1]]
    template_height, template_width = len(template), len(template[0])
    center_row, center_col = template_height // 2, template_width // 2
    if template[center_row][center_col] == background:
        return [row[:] for row in grid]
    marker = template[center_row][center_col]
    output = [row[:] for row in grid]
    for row in range(top, bottom + 1):
        for col in range(left, right + 1):
            output[row][col] = background
    for component in components[1:]:
        rows = [row for row, _ in component]
        cols = [col for _, col in component]
        target_top, target_bottom = min(rows), max(rows)
        target_left, target_right = min(cols), max(cols)
        for anchor_row, anchor_col in component:
            if grid[anchor_row][anchor_col] != marker:
                continue
            for motif_row in range(template_height):
                for motif_col in range(template_width):
                    colour = template[motif_row][motif_col]
                    if colour == background:
                        continue
                    row = anchor_row + motif_row - center_row
                    col = anchor_col + motif_col - center_col
                    if target_top <= row <= target_bottom and target_left <= col <= target_right:
                        output[row][col] = colour
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                first_row, first_col = center_row + dr, center_col + dc
                second_row, second_col = center_row + 2 * dr, center_col + 2 * dc
                if not (0 <= second_row < template_height and 0 <= second_col < template_width):
                    continue
                first_colour = template[first_row][first_col]
                if first_colour == background or first_colour != template[second_row][second_col]:
                    continue
                row, col = anchor_row + dr, anchor_col + dc
                while target_top <= row <= target_bottom and target_left <= col <= target_right:
                    output[row][col] = first_colour
                    row += dr
                    col += dc
            output[anchor_row][anchor_col] = marker
    return output
