def _select_unique_asymmetric_panel(grid):
    height, width = len(grid), len(grid[0])
    if height % width == 0:
        size = width
        panels = [grid[row : row + size] for row in range(0, height, size)]
    elif width % height == 0:
        size = height
        panels = [
            [grid[row][col : col + size] for row in range(height)] for col in range(0, width, size)
        ]
    else:
        return [row[:] for row in grid]
    asymmetric = [
        panel
        for panel in panels
        if any(panel[row][col] != panel[col][row] for row in range(size) for col in range(size))
    ]
    return asymmetric[0] if len(asymmetric) == 1 else [row[:] for row in grid]


def solve(grid):
    return _select_unique_asymmetric_panel(grid)
