def solve(grid):
    source = [list(row) for row in grid]
    height = len(source)
    width = len(source[0]) if height else 0
    seen = set()
    components = []
    for row in range(height):
        for col in range(width):
            if source[row][col] == 0 or (row, col) in seen:
                continue
            seen.add((row, col))
            stack = [(row, col)]
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
                        and source[next_row][next_col]
                        and (next_row, next_col) not in seen
                    ):
                        seen.add((next_row, next_col))
                        stack.append((next_row, next_col))
            if len({source[row][col] for row, col in component}) == 4:
                components.append(component)
    if not components:
        return source
    output = [row[:] for row in source]
    for component in components:
        for row, col in component:
            output[row][col] = 0
    for component in components:
        top = min(row for row, _ in component)
        left = min(col for _, col in component)
        bottom = max(row for row, _ in component)
        right = max(col for _, col in component)
        template = [row[left : right + 1] for row in source[top : bottom + 1]]
        colors = {}
        for row in template:
            for color in row:
                if color:
                    colors[color] = colors.get(color, 0) + 1
        paint_color = min(colors, key=lambda color: (-colors[color], color))
        source_cells = set(component)
        variants = []
        for turns in range(4):
            variant = template
            for _ in range(turns):
                variant = [list(row) for row in zip(*variant[::-1])]
            for candidate in (variant, [row[::-1] for row in variant]):
                if candidate not in variants:
                    variants.append(candidate)
        for variant in variants:
            variant_height = len(variant)
            variant_width = len(variant[0])
            keys = [
                (row, col)
                for row in range(variant_height)
                for col in range(variant_width)
                if variant[row][col] and variant[row][col] != paint_color
            ]
            paint = [
                (row, col)
                for row in range(variant_height)
                for col in range(variant_width)
                if variant[row][col] == paint_color
            ]
            for row in range(height - variant_height + 1):
                for col in range(width - variant_width + 1):
                    if not keys or any(
                        source[row + key_row][col + key_col] != variant[key_row][key_col]
                        for key_row, key_col in keys
                    ):
                        continue
                    if not any(
                        (row + key_row, col + key_col) not in source_cells
                        for key_row, key_col in keys
                    ):
                        continue
                    for paint_row, paint_col in paint:
                        output[row + paint_row][col + paint_col] = paint_color
    return output
