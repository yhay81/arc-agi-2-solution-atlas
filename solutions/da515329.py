from collections import Counter

DIRECTIONS = ((-1, 0), (0, 1), (1, 0), (0, -1))
NEIGHBORS = tuple((dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1))


def _parse(grid):
    counts = Counter(value for row in grid for value in row)
    if len(counts) != 2:
        raise ValueError("Expected one background and one line color")
    background = counts.most_common(1)[0][0]
    color = next(value for value in counts if value != background)
    points = {
        (row, col)
        for row, line in enumerate(grid)
        for col, value in enumerate(line)
        if value == color
    }
    top, bottom = min(row for row, _ in points), max(row for row, _ in points)
    left, right = min(col for _, col in points), max(col for _, col in points)
    center = (top + bottom) // 2, (left + right) // 2
    length = (bottom - top) // 2
    expected = {
        (center[0] + dr * step, center[1] + dc * step)
        for dr, dc in DIRECTIONS
        for step in range(1, length + 1)
    }
    if (bottom - top) % 2 or right - left != 2 * length or length < 1 or points != expected:
        raise ValueError("Expected a four-arm cross with a blank center")
    return color, center, length


def _rotations(point):
    row, col = point
    for _ in range(4):
        yield row, col
        row, col = col, -row


def solve(grid):
    color, (center_row, center_col), length = _parse(grid)
    height, width = len(grid), len(grid[0])
    paths = [[(dr * step, dc * step) for step in range(1, length + 1)] for dr, dc in DIRECTIONS]
    occupied = {point for path in paths for point in path}
    head = paths[0][-1]
    previous = paths[0][-2:]
    heading = 0
    output = [row[:] for row in grid]

    turns_outside = 0
    tick = 0
    while True:
        allowed = set(previous)
        for direction in ((heading + 1) % 4, heading, (heading - 1) % 4):
            dr, dc = DIRECTIONS[direction]
            candidate = head[0] + dr, head[1] + dc
            if all(
                (candidate[0] + nr, candidate[1] + nc) not in occupied
                or (candidate[0] + nr, candidate[1] + nc) in allowed
                for nr, nc in NEIGHBORS
            ):
                break
        else:
            raise ValueError(f"No legal continuation at tick {tick}")

        proposals = tuple(_rotations(candidate))
        if any(
            max(abs(first[0] - second[0]), abs(first[1] - second[1])) <= 1
            for index, first in enumerate(proposals)
            for second in proposals[index + 1 :]
        ):
            raise ValueError("Simultaneous path collision")
        visible = False
        for row, col in proposals:
            row += center_row
            col += center_col
            if 0 <= row < height and 0 <= col < width:
                output[row][col] = color
                visible = True
        if visible:
            turns_outside = 0
        elif direction == (heading + 1) % 4:
            turns_outside += 1
        elif direction != heading:
            turns_outside -= 1
        if not visible and turns_outside >= 4:
            return output

        occupied.update(proposals)
        head, heading = candidate, direction
        previous = (previous + [candidate])[-2:]
        tick += 1
