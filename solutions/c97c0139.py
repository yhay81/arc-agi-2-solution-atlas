def components(points):
    remaining, result = set(points), []
    while remaining:
        start = min(remaining)
        remaining.remove(start)
        group, stack = {start}, [start]
        while stack:
            r, c = stack.pop()
            for neighbor in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if neighbor in remaining:
                    remaining.remove(neighbor)
                    group.add(neighbor)
                    stack.append(neighbor)
        result.append(group)
    return result


def bounds(points):
    return (
        min(r for r, c in points),
        max(r for r, c in points),
        min(c for r, c in points),
        max(c for r, c in points),
    )


def solve(grid):
    red = {(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == 2}
    out = [row[:] for row in grid]
    for group in components(red):
        top, bottom, left, right = bounds(group)
        if top != bottom and left != right:
            raise ValueError("Expected a straight red bar")
        length = len(group)
        if length != max(bottom - top + 1, right - left + 1):
            raise ValueError("Expected a solid red bar")
        for distance in range(1, (length + 1) // 2):
            for offset in range(distance, length - distance):
                for side in (-1, 1):
                    r, c = (
                        (top + side * distance, left + offset)
                        if top == bottom
                        else (top + offset, left + side * distance)
                    )
                    if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 0:
                        out[r][c] = 8
    return out
