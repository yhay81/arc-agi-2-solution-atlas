def solve(grid):
    h, w = len(grid), len(grid[0])
    components = []
    seen = set()
    for row0 in range(h):
        for col0 in range(w):
            if grid[row0][col0] != 5 or (row0, col0) in seen:
                continue
            stack = [(row0, col0)]
            seen.add((row0, col0))
            component = []
            while stack:
                row, col = stack.pop()
                component.append((row, col))
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        neighbor = (row + dr, col + dc)
                        if (
                            (dr or dc)
                            and 0 <= neighbor[0] < h
                            and 0 <= neighbor[1] < w
                            and grid[neighbor[0]][neighbor[1]] == 5
                            and neighbor not in seen
                        ):
                            seen.add(neighbor)
                            stack.append(neighbor)
            if len(component) >= 2:
                rows = [row for row, _ in component]
                cols = [col for _, col in component]
                score = len(component) * sum(row * col for row, col in component) - sum(rows) * sum(
                    cols
                )
                if score:
                    components.append((component, score))
    positive = sum(len(component) for component, score in components if score > 0)
    negative = sum(len(component) for component, score in components if score < 0)
    if not positive or not negative or positive == negative:
        return [row[:] for row in grid]
    dominant_sign = positive > negative
    output = [row[:] for row in grid]
    for component, score in components:
        color = 8 if (score > 0) == dominant_sign else 2
        for row, col in component:
            output[row][col] = color
    return output
