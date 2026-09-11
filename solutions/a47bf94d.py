from collections import Counter

DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
SPECIAL = {5, 8, 9}


def _special(grid, point):
    row, col = point
    return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] in SPECIAL


def _components(grid, color):
    remaining = {
        (row, col)
        for row, values in enumerate(grid)
        for col, value in enumerate(values)
        if value == color
    }
    found = []
    while remaining:
        start = min(remaining)
        remaining.remove(start)
        stack = [start]
        cells = []
        while stack:
            row, col = stack.pop()
            cells.append((row, col))
            for dr, dc in DIRECTIONS:
                point = row + dr, col + dc
                if point in remaining:
                    remaining.remove(point)
                    stack.append(point)
        found.append(cells)
    return found


def _tips(grid):
    tips = {}
    for row, values in enumerate(grid):
        for col, value in enumerate(values):
            if value != 8:
                continue
            neighbors = [
                direction
                for direction in DIRECTIONS
                if _special(grid, (row + direction[0], col + direction[1]))
            ]
            if len(neighbors) == 1:
                tips[row, col] = neighbors[0]
    return tips


def _trace(grid, start, tips, blocks, blockmap):
    position, direction = start, tips[start]
    seen = set()
    while (position, direction) not in seen:
        seen.add((position, direction))
        forward = position[0] + direction[0], position[1] + direction[1]
        if _special(grid, forward) and grid[forward[0]][forward[1]] == 9:
            block = blocks[blockmap[forward]]
            block_set = set(block)
            next_position = forward
            while next_position in block_set:
                next_position = (
                    next_position[0] + direction[0],
                    next_position[1] + direction[1],
                )
            if _special(grid, next_position):
                position = next_position
                continue
            exits = []
            for row, col in block:
                for dr, dc in DIRECTIONS:
                    candidate = row + dr, col + dc
                    item = candidate, (dr, dc)
                    if (
                        candidate != position
                        and candidate not in block_set
                        and _special(grid, candidate)
                        and item not in exits
                    ):
                        exits.append(item)
            if len(exits) != 1:
                raise ValueError(exits)
            position, direction = exits[0]
            continue
        if _special(grid, forward):
            position = forward
            continue
        turns = [
            candidate
            for candidate in DIRECTIONS
            if candidate != (-direction[0], -direction[1])
            and _special(grid, (position[0] + candidate[0], position[1] + candidate[1]))
        ]
        if not turns:
            return position
        if len(turns) != 1:
            raise ValueError("task assumptions are not satisfied")
        direction = turns[0]
        position = position[0] + direction[0], position[1] + direction[1]
    raise ValueError("wire cycle")


def _center(tips, end):
    dr, dc = -tips[end][0], -tips[end][1]
    return (end[0] + 2 * dr, end[1] + 2 * dc), (dr, dc)


def _endpoint_color(grid, tips, ends, background):
    colors = set()
    for end in ends:
        center, _ = _center(tips, end)
        for row in range(max(0, center[0] - 1), min(len(grid), center[0] + 2)):
            for col in range(max(0, center[1] - 1), min(len(grid[0]), center[1] + 2)):
                if grid[row][col] not in SPECIAL and grid[row][col] != background:
                    colors.add(grid[row][col])
    if len(colors) != 1:
        raise ValueError(colors)
    return next(iter(colors))


def _draw_end(output, tips, end, color):
    center, (dr, dc) = _center(tips, end)
    offsets = DIRECTIONS if dr < 0 or dc < 0 else ((0, 0), (-1, -1), (-1, 1), (1, -1), (1, 1))
    for row_offset, col_offset in offsets:
        row, col = center[0] + row_offset, center[1] + col_offset
        if 0 <= row < len(output) and 0 <= col < len(output[0]):
            output[row][col] = color


def solve(grid):
    background = Counter(value for row in grid for value in row).most_common(1)[0][0]
    blocks = _components(grid, 9)
    blockmap = {point: index for index, block in enumerate(blocks) for point in block}
    tips = _tips(grid)
    output = [[value if value in SPECIAL else background for value in row] for row in grid]
    seen = set()
    for tip in tips:
        if tip in seen:
            continue
        other = _trace(grid, tip, tips, blocks, blockmap)
        if other not in tips or other == tip:
            raise ValueError("task assumptions are not satisfied")
        ends = tip, other
        seen.update(ends)
        color = _endpoint_color(grid, tips, ends, background)
        for end in ends:
            _draw_end(output, tips, end, color)
    return output


DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
