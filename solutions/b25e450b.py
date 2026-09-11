def solve(grid):
    height, width = len(grid), len(grid[0])
    values = {value for row in grid for value in row}
    if len(values) < 2:
        return [row[:] for row in grid]
    counts = {value: sum(row.count(value) for row in grid) for value in values}
    background = 7 if 7 in values else max(values, key=counts.get)
    marker = 0 if 0 in values else min(values, key=counts.get)
    if marker == background:
        return [row[:] for row in grid]
    occupied = {
        (row, col) for row in range(height) for col in range(width) if grid[row][col] == marker
    }
    components = []
    while occupied:
        stack = [occupied.pop()]
        component = []
        while stack:
            row, col = stack.pop()
            component.append((row, col))
            for next_cell in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
                if next_cell in occupied:
                    occupied.remove(next_cell)
                    stack.append(next_cell)
        rows = [row for row, _ in component]
        cols = [col for _, col in component]
        if min(rows) == 0 or max(rows) == height - 1 or min(cols) == 0 or max(cols) == width - 1:
            components.append(component)
    if not components:
        return [row[:] for row in grid]
    output = [row[:] for row in grid]
    bounds = []
    for component in components:
        rows = [row for row, _ in component]
        cols = [col for _, col in component]
        top, bottom, left, right = min(rows), max(rows), min(cols), max(cols)
        bounds.append((top, bottom, left, right))
        if top == 0 or bottom == height - 1:
            for row in range(height):
                for col in range(left, right + 1):
                    output[row][col] = background
        if left == 0 or right == width - 1:
            for row in range(top, bottom + 1):
                for col in range(width):
                    output[row][col] = background
    for top, bottom, left, right in bounds:
        component_height, component_width = bottom - top + 1, right - left + 1
        if top == 0:
            target_top = height - component_height
            for row in range(component_height):
                for col in range(component_width):
                    if grid[top + row][left + col] == marker:
                        output[target_top + row][left + col] = marker
        elif bottom == height - 1:
            for row in range(component_height):
                for col in range(component_width):
                    if grid[top + row][left + col] == marker:
                        output[row][left + col] = marker
        if left == 0:
            target_left = width - component_width
            for row in range(component_height):
                for col in range(component_width):
                    if grid[top + row][left + col] == marker:
                        output[top + row][target_left + col] = marker
        elif right == width - 1:
            for row in range(component_height):
                for col in range(component_width):
                    if grid[top + row][left + col] == marker:
                        output[top + row][col] = marker
    return output
