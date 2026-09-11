def _cycle_concentric_ring_colors(array):
    if not array or len(array) != len(array[0]):
        return [r[:] for r in array]
    size = len(array)
    ring_colors: list[int] = []
    for inset in range((size + 1) // 2):
        cells = [
            array[row][col]
            for row in range(inset, size - inset)
            for col in range(inset, size - inset)
            if row in (inset, size - inset - 1) or col in (inset, size - inset - 1)
        ]
        if len(set(cells)) != 1:
            return [r[:] for r in array]
        ring_colors.append(cells[0])
    ordered_colors: list[int] = []
    for color in ring_colors:
        if color not in ordered_colors:
            ordered_colors.append(color)
    if len(ordered_colors) < 3:
        return [r[:] for r in array]
    mapping = {
        color: ordered_colors[(index - 1) % len(ordered_colors)]
        for index, color in enumerate(ordered_colors)
    }
    output = [r[:] for r in array]
    source_copy = [r[:] for r in array]
    for source, destination in mapping.items():
        for r in range(size):
            for c in range(size):
                if source_copy[r][c] == source:
                    output[r][c] = destination
    return output


def solve(grid):
    return _cycle_concentric_ring_colors([r[:] for r in grid])
