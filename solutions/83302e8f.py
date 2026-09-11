def solve(grid):
    line_color = -1
    isolated_color = 3
    merged_color = 4
    background_color = 0
    if line_color < 0:
        line_colors = sorted({value for row in grid for value in row if value != background_color})
        if len(line_colors) != 1:
            return [row[:] for row in grid]
        line_color = line_colors[0]
    height, width = len(grid), len(grid[0])
    seen = set()
    components = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] != background_color or (row, col) in seen:
                continue
            component = {(row, col)}
            seen.add((row, col))
            stack = [(row, col)]
            while stack:
                current_row, current_col = stack.pop()
                for row_delta, col_delta in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    neighbor = (current_row + row_delta, current_col + col_delta)
                    if not (
                        0 <= neighbor[0] < height
                        and 0 <= neighbor[1] < width
                        and grid[neighbor[0]][neighbor[1]] == background_color
                        and (neighbor not in seen)
                    ):
                        continue
                    seen.add(neighbor)
                    component.add(neighbor)
                    stack.append(neighbor)
            components.append(component)
    if not components:
        return [row[:] for row in grid]
    sizes = [len(component) for component in components]
    counts = {size: sizes.count(size) for size in set(sizes)}
    nominal_size = max(counts, key=lambda size: (counts[size], -size))
    output = [row[:] for row in grid]
    for component in components:
        color = isolated_color if len(component) == nominal_size else merged_color
        for row, col in component:
            output[row][col] = color
    return output
