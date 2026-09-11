from collections import Counter


def solve(grid):
    height, width = len(grid), len(grid[0])
    counts = Counter(value for row in grid for value in row)
    background = counts.most_common(1)[0][0]
    foreground = [value for value in counts if value != background]
    if len(foreground) != 1:
        return [row[:] for row in grid]
    color = foreground[0]
    seen = set()
    summaries = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] != color or (row, col) in seen:
                continue
            stack = [(row, col)]
            seen.add((row, col))
            component = []
            while stack:
                r, c = stack.pop()
                component.append((r, c))
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        rr, cc = r + dr, c + dc
                        if (
                            0 <= rr < height
                            and 0 <= cc < width
                            and grid[rr][cc] == color
                            and (rr, cc) not in seen
                        ):
                            seen.add((rr, cc))
                            stack.append((rr, cc))
            sums = {r + c for r, c in component}
            if len(sums) != 1:
                return [row[:] for row in grid]
            differences = [c - r for r, c in component]
            summaries.append((next(iter(sums)), min(differences), max(differences)))
    if len(summaries) < 2:
        return [row[:] for row in grid]
    summaries.sort()
    output = [row[:] for row in grid]
    for row in range(height):
        for col in range(width):
            if grid[row][col] != background:
                continue
            diagonal_sum, difference = row + col, col - row
            left = [
                item
                for item in summaries
                if item[0] <= diagonal_sum and item[1] <= difference <= item[2]
            ]
            right = [
                item
                for item in summaries
                if item[0] >= diagonal_sum and item[1] <= difference <= item[2]
            ]
            if left and right and left[-1][0] < right[0][0]:
                output[row][col] = 2
    return output
