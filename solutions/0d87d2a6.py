from itertools import combinations


def _red_components(grid):
    unseen = {
        (row, col) for row, line in enumerate(grid) for col, value in enumerate(line) if value == 2
    }
    result = []
    while unseen:
        start = unseen.pop()
        component = {start}
        queue = [start]
        for row, col in queue:
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                neighbor = row + dr, col + dc
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    component.add(neighbor)
                    queue.append(neighbor)
        result.append(component)
    return result


def solve(grid):
    height, width = len(grid), len(grid[0])
    markers = {
        (row, col) for row, line in enumerate(grid) for col, value in enumerate(line) if value == 1
    }
    lines = set()
    for first, second in combinations(markers, 2):
        if first[0] == second[0] and {first[1], second[1]} == {0, width - 1}:
            lines.update((first[0], col) for col in range(width))
        elif first[1] == second[1] and {first[0], second[0]} == {0, height - 1}:
            lines.update((row, first[1]) for row in range(height))
    adjacent = lines | {
        (row + dr, col + dc) for row, col in lines for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1))
    }
    output = [row[:] for row in grid]
    for component in _red_components(grid):
        if component & adjacent:
            for row, col in component:
                output[row][col] = 1
    for row, col in lines:
        output[row][col] = 1
    return output
