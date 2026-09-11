from math import gcd


def solve(grid):
    colors = sorted({value for row in grid for value in row if value})
    if len(colors) != 2:
        return [row[:] for row in grid]

    def components(color):
        occupied = {
            (r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == color
        }
        found = []
        while occupied:
            start = occupied.pop()
            stack, component = [start], [start]
            while stack:
                r, c = stack.pop()
                for neighbor in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if neighbor in occupied:
                        occupied.remove(neighbor)
                        stack.append(neighbor)
                        component.append(neighbor)
            found.append(component)
        return found

    def score(color):
        total = largest = 0
        for component in components(color):
            rows = [r for r, _ in component]
            cols = [c for _, c in component]
            area = (max(rows) - min(rows) + 1) * (max(cols) - min(cols) + 1)
            if area == len(component) and area >= 4:
                total += area
                largest = max(largest, area)
        return total, largest

    mask_color, marker_color = sorted(colors, key=score, reverse=True)
    if score(mask_color) == (0, 0):
        return [row[:] for row in grid]
    positions = [
        (r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == mask_color
    ]
    top = min(r for r, _ in positions)
    bottom = max(r for r, _ in positions)
    left = min(c for _, c in positions)
    right = max(c for _, c in positions)
    mask = [
        [grid[r][c] == mask_color for c in range(left, right + 1)] for r in range(top, bottom + 1)
    ]

    runs = []
    for rows in (mask, list(map(list, zip(*mask)))):
        if rows:
            start = 0
            for index in range(1, len(rows)):
                if rows[index] != rows[index - 1]:
                    runs.append(index - start)
                    start = index
            runs.append(len(rows) - start)
    if not runs:
        return [row[:] for row in grid]
    unit = runs[0]
    for length in runs[1:]:
        unit = gcd(unit, length)
    if unit < 1 or len(mask) % unit or len(mask[0]) % unit:
        return [row[:] for row in grid]
    return [
        [
            marker_color
            if any(mask[r * unit + dr][c * unit + dc] for dr in range(unit) for dc in range(unit))
            else 0
            for c in range(len(mask[0]) // unit)
        ]
        for r in range(len(mask) // unit)
    ]
