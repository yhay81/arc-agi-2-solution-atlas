def solve(grid):
    height = len(grid)
    width = len(grid[0])
    output = [row[:] for row in grid]
    seen = set()
    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
    labels = {"one_turn": 1, "multi_turn": 6, "branch": 2}
    for row in range(height):
        for col in range(width):
            if grid[row][col] != 3 or (row, col) in seen:
                continue
            component = []
            stack = [(row, col)]
            seen.add((row, col))
            while stack:
                current = stack.pop()
                component.append(current)
                for drow, dcol in directions:
                    neighbor = (current[0] + drow, current[1] + dcol)
                    if (
                        0 <= neighbor[0] < height
                        and 0 <= neighbor[1] < width
                        and grid[neighbor[0]][neighbor[1]] == 3
                        and neighbor not in seen
                    ):
                        seen.add(neighbor)
                        stack.append(neighbor)
            points = set(component)
            neighbors = {
                point: [
                    (point[0] + drow, point[1] + dcol)
                    for drow, dcol in directions
                    if (point[0] + drow, point[1] + dcol) in points
                ]
                for point in points
            }
            if any(len(neighbors[point]) >= 3 for point in points):
                topology = "branch"
            else:
                endpoints = [point for point in points if len(neighbors[point]) == 1]
                if len(endpoints) != 2:
                    continue
                previous = None
                current = endpoints[0]
                steps = []
                while True:
                    next_points = [point for point in neighbors[current] if point != previous]
                    if not next_points:
                        break
                    next_point = next_points[0]
                    steps.append((next_point[0] - current[0], next_point[1] - current[1]))
                    previous, current = current, next_point
                    if current == endpoints[1]:
                        break
                bends = sum(first != second for first, second in zip(steps, steps[1:]))
                topology = "one_turn" if bends == 1 else "multi_turn"
            for row, col in component:
                output[row][col] = labels[topology]
    return output
