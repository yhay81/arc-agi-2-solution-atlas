def solve(grid):
    height, width = len(grid), len(grid[0])
    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = max(counts, key=counts.get)
    seen = set()
    components = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] == background or (row, col) in seen:
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
                            and grid[rr][cc] != background
                            and (rr, cc) not in seen
                        ):
                            seen.add((rr, cc))
                            stack.append((rr, cc))
            components.append(cells)
    total = sum(len(cells) for cells in components)
    size = int(total**0.5)
    if not (size * size == total):
        raise ValueError("task assumptions are not satisfied")
    variants = []
    for cells in components:
        origin_r = min(r for r, _ in cells)
        origin_c = min(c for _, c in cells)
        points = [(r - origin_r, c - origin_c) for r, c in cells]
        values = [grid[r][c] for r, c in cells]
        component_variants = []
        for turns in range(4):
            rotated = points
            for _ in range(turns):
                rotated = [(c, -r) for r, c in rotated]
            min_r = min(r for r, _ in rotated)
            min_c = min(c for _, c in rotated)
            rotated = [(r - min_r, c - min_c) for r, c in rotated]
            order = sorted(range(len(rotated)), key=lambda i: rotated[i])
            component_variants.append(
                ([(rotated[i][0], rotated[i][1]) for i in order], [values[i] for i in order])
            )
        variants.append(component_variants)
    output = [[-1] * size for _ in range(size)]
    solutions = []

    def search(left):
        if len(solutions) > 2:
            return
        if not left:
            if output[0][0] == 5:
                solutions.append([row[:] for row in output])
            return
        first = next((r, c) for r in range(size) for c in range(size) if output[r][c] < 0)
        for index in left:
            for rotated, vals in variants[index]:
                shifted = [
                    (r + first[0] - rotated[0][0], c + first[1] - rotated[0][1]) for r, c in rotated
                ]
                if any(r < 0 or r >= size or c < 0 or c >= size for r, c in shifted):
                    continue
                if any(output[r][c] != -1 for r, c in shifted):
                    continue
                if first == (0, 0) and vals[0] != 5:
                    continue
                for (r, c), value in zip(shifted, vals):
                    output[r][c] = value
                search([i for i in left if i != index])
                for r, c in shifted:
                    output[r][c] = -1

    search(list(range(len(variants))))
    unique = {str(solution): solution for solution in solutions}
    if not (len(unique) == 1):
        raise ValueError(f"{len(unique)} distinct rotation-only assemblies")
    return next(iter(unique.values()))
