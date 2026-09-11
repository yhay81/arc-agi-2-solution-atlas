from collections import Counter
from math import gcd


def _horizontal(grid):
    height, width = len(grid), len(grid[0])
    counts = Counter(value for row in grid for value in row)
    background = min(counts, key=lambda value: (-counts[value], value))
    foreground = [value for value in counts if value != background]
    if len(foreground) != 1:
        return [row[:] for row in grid]
    color = foreground[0]
    bars = []
    for row in range(height):
        runs = []
        start = None
        for col in range(width + 1):
            occupied = col < width and grid[row][col] == color
            if occupied and start is None:
                start = col
            elif not occupied and start is not None:
                if col - start >= 2:
                    runs.append((start, col - 1))
                start = None
        if runs:
            left, right = max(runs, key=lambda item: item[1] - item[0])
            bars.append((row, left, right))
    if len(bars) < 2:
        return [row[:] for row in grid]

    period = 0
    for (first, _, _), (second, _, _) in zip(bars, bars[1:]):
        period = gcd(period, second - first)
    first_row, first_left, first_right = bars[0]
    second_row, second_left, second_right = bars[1]
    row_delta = second_row - first_row
    left_delta = (second_left - first_left) * period // row_delta
    right_delta = (second_right - first_right) * period // row_delta
    for row, left, right in bars:
        if (row - first_row) % period:
            return [row[:] for row in grid]
        step = (row - first_row) // period
        if left != first_left + left_delta * step or right != first_right + right_delta * step:
            return [row[:] for row in grid]

    can_extend_up = first_row - period >= 0
    can_extend_down = bars[-1][0] + period < height
    if can_extend_up == can_extend_down:
        return [row[:] for row in grid]
    sequence = []
    for row in range(first_row % period, height, period):
        step = (row - first_row) // period
        sequence.append((row, first_left + left_delta * step, first_right + right_delta * step))

    output = [[5] * width for _ in range(height)]
    for row, left, right in sequence:
        for col in range(max(0, left), min(width, right + 1)):
            output[row][col] = color
    endpoints = []
    if left_delta:
        endpoints.append("left")
    if right_delta:
        endpoints.append("right")
    for row, left, right in sequence:
        points = (
            [left]
            if endpoints == ["left"]
            else [right]
            if endpoints == ["right"]
            else [left, right]
        )
        rail_rows = range(row + 1) if can_extend_down else range(row, height)
        for col in points:
            if 0 <= col < width:
                for rail_row in rail_rows:
                    output[rail_row][col] = color
    return output


def _transpose(grid):
    return [list(row) for row in zip(*grid)]


def solve(grid):
    result = _horizontal(grid)
    return result if result != grid else _transpose(_horizontal(_transpose(grid)))
