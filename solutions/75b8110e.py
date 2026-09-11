def _compose_quadrants_priority(array, order=(1, 2, 3, 0)):
    h, w = len(array), len(array[0])
    if h % 2 or w % 2:
        return [row[:] for row in array]
    height, width = h // 2, w // 2
    panels = (
        [row[:width] for row in array[:height]],
        [row[width:] for row in array[:height]],
        [row[:width] for row in array[height:]],
        [row[width:] for row in array[height:]],
    )
    if sorted(int(index) for index in order) != [0, 1, 2, 3]:
        return [row[:] for row in array]
    output = [[0] * width for _ in range(height)]
    for index in order:
        panel = panels[int(index)]
        for r in range(height):
            for c in range(width):
                if output[r][c] == 0 and panel[r][c] != 0:
                    output[r][c] = panel[r][c]
    return output


def solve(grid):
    return _compose_quadrants_priority(grid, (1, 2, 3, 0))
