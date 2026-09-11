def solve(grid):
    height, width = len(grid), len(grid[0])
    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = max(counts, key=counts.get)
    objects = []
    for color in counts:
        if color == background:
            continue
        seen = set()
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
                            rr, cc = r + dr, c + dc
                            if (
                                0 <= rr < height
                                and 0 <= cc < width
                                and grid[rr][cc] == color
                                and (rr, cc) not in seen
                            ):
                                seen.add((rr, cc))
                                stack.append((rr, cc))
                objects.append((color, cells))
    total = sum(len(cells) for _, cells in objects)
    size = total // 4 + 1
    if not (total == 4 * (size - 1)):
        raise ValueError("task assumptions are not satisfied")
    border = {
        (r, c) for r in range(size) for c in range(size) if r in (0, size - 1) or c in (0, size - 1)
    }
    options = []
    for color, cells in objects:
        min_row = min(r for r, _ in cells)
        min_col = min(c for _, c in cells)
        points = [(r - min_row, c - min_col) for r, c in cells]
        placements = []
        for row in range(size - max(r for r, _ in points)):
            for col in range(size - max(c for _, c in points)):
                placed = {(row + r, col + c) for r, c in points}
                if placed <= border:
                    placements.append(placed)
        options.append((color, placements))
    options.sort(key=lambda item: len(item[1]))
    solutions = []

    def search(index, used, chosen):
        if len(solutions) > 2:
            return
        if index == len(options):
            if used == border:
                solutions.append(chosen[:])
            return
        color, placements = options[index]
        for placed in placements:
            if used & placed:
                continue
            search(index + 1, used | placed, chosen + [(color, placed)])

    search(0, set(), [])
    if not (len(solutions) == 1):
        raise ValueError("task assumptions are not satisfied")
    output = [[background] * size for _ in range(size)]
    for color, cells in solutions[0]:
        for row, col in cells:
            output[row][col] = color
    return output
