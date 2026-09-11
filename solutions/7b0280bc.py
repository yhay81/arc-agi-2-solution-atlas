import heapq
from collections import Counter


def solve(grid):
    height, width = len(grid), len(grid[0])
    background = Counter(value for row in grid for value in row).most_common(1)[0][0]
    colors = set(value for row in grid for value in row) - {background}

    def components(color, diagonal):
        seen = set()
        groups = []
        for row in range(height):
            for col in range(width):
                if grid[row][col] != color or (row, col) in seen:
                    continue
                stack = [(row, col)]
                seen.add((row, col))
                cells = []
                while stack:
                    r, c = stack.pop()
                    cells.append((r, c))
                    for dr in (-1, 0, 1):
                        for dc in (-1, 0, 1):
                            if not diagonal and dr and dc:
                                continue
                            rr, cc = r + dr, c + dc
                            if (
                                0 <= rr < height
                                and 0 <= cc < width
                                and grid[rr][cc] == color
                                and (rr, cc) not in seen
                            ):
                                seen.add((rr, cc))
                                stack.append((rr, cc))
                groups.append(cells)
        return groups

    def square(cells):
        top, left = min(r for r, _ in cells), min(c for _, c in cells)
        bottom, right = max(r for r, _ in cells), max(c for _, c in cells)
        return (
            bottom - top == right - left
            and len(cells) == (bottom - top + 1) ** 2
            and len(cells) > 1
        )

    terminal = next(
        color
        for color in colors
        if len(components(color, False)) == 2
        and all(square(cells) for cells in components(color, False))
    )
    rest = colors - {terminal}
    node = next(color for color in rest if all(square(cells) for cells in components(color, False)))
    path = next(iter(rest - {node}))
    parts = []
    types = []
    for color in (terminal, node, path):
        for cells in components(color, color == path):
            parts.append(cells)
            types.append(color)
    owner = [[-1] * width for _ in range(height)]
    for index, cells in enumerate(parts):
        for row, col in cells:
            owner[row][col] = index
    adjacency = [set() for _ in parts]
    for row in range(height):
        for col in range(width):
            index = owner[row][col]
            if index < 0:
                continue
            for rr in range(max(0, row - 1), min(height, row + 2)):
                for cc in range(max(0, col - 1), min(width, col + 2)):
                    other = owner[rr][cc]
                    if other >= 0 and other != index:
                        adjacency[index].add(other)
    ends = [index for index, color in enumerate(types) if color == terminal]
    if not (len(ends) == 2):
        raise ValueError("task assumptions are not satisfied")
    queue = [(0, 0, ends[0], [])]
    best = {}
    while queue:
        nodes, distance, index, history = heapq.heappop(queue)
        if index in best:
            continue
        best[index] = (nodes, distance)
        history = history + [index]
        if index == ends[1]:
            break
        for other in adjacency[index]:
            heapq.heappush(
                queue,
                (nodes + (types[other] == node), distance + len(parts[other]), other, history),
            )
    if not (index == ends[1]):
        raise ValueError("task assumptions are not satisfied")
    output = [row[:] for row in grid]
    for index in history:
        if types[index] != terminal:
            color = 3 if types[index] == node else 5
            for row, col in parts[index]:
                output[row][col] = color
    return output
