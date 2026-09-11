def solve(grid):
    from collections import Counter

    height, width = len(grid), len(grid[0])
    background = Counter(value for row in grid for value in row).most_common(1)[0][0]
    output = [[background] * width for _ in grid]
    for color in {value for row in grid for value in row} - {background}:
        remaining = {
            (r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == color
        }
        while remaining:
            component = {remaining.pop()}
            stack = list(component)
            while stack:
                r, c = stack.pop()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    point = r + dr, c + dc
                    if point in remaining:
                        remaining.remove(point)
                        component.add(point)
                        stack.append(point)
            top = min(r for r, c in component)
            left = min(c for r, c in component)
            if (
                len(component) != 3
                or max(r for r, c in component) - top != 1
                or max(c for r, c in component) - left != 1
            ):
                raise ValueError("Expected isolated 2x2 L-shaped triomino")
            normalized = {(r - top, c - left) for r, c in component}
            missing = ({(0, 0), (0, 1), (1, 0), (1, 1)} - normalized).pop()
            r = 0 if missing[0] == 1 else height - 1
            c = 0 if missing[1] == 1 else width - 1
            for k in range(height // 2):
                output[r + k * (1 if r == 0 else -1)][c] = color
            for k in range(width // 2):
                output[r][c + k * (1 if c == 0 else -1)] = color
    return output
