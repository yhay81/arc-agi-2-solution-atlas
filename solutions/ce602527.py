def solve(grid):
    height, width = len(grid), len(grid[0])
    values = sorted({value for row in grid for value in row})
    background = max(values, key=lambda value: sum(cell == value for row in grid for cell in row))
    objects = []
    seen = set()
    for row in range(height):
        for col in range(width):
            if grid[row][col] == background or (row, col) in seen:
                continue
            stack = [(row, col)]
            seen.add((row, col))
            component = []
            while stack:
                current_row, current_col = stack.pop()
                component.append((current_row, current_col))
                for next_row, next_col in (
                    (current_row - 1, current_col),
                    (current_row + 1, current_col),
                    (current_row, current_col - 1),
                    (current_row, current_col + 1),
                ):
                    if (
                        0 <= next_row < height
                        and 0 <= next_col < width
                        and grid[next_row][next_col] != background
                        and (next_row, next_col) not in seen
                    ):
                        seen.add((next_row, next_col))
                        stack.append((next_row, next_col))
            top = min(r for r, _ in component)
            bottom = max(r for r, _ in component)
            left = min(c for _, c in component)
            right = max(c for _, c in component)
            crop = [grid[r][left : right + 1] for r in range(top, bottom + 1)]
            mask = tuple(tuple(cell != background for cell in row) for row in crop)
            objects.append((crop, mask))
    if not objects:
        return [row[:] for row in grid]
    ranked = []
    for index, (crop, mask) in enumerate(objects):
        doubled = [
            [mask[row // 2][col // 2] for col in range(len(mask[0]) * 2)]
            for row in range(len(mask) * 2)
        ]
        shapes = set()
        occurrences = 0
        for target_index, (_, target) in enumerate(objects):
            if (
                target_index == index
                or len(target) > len(doubled)
                or len(target[0]) > len(doubled[0])
            ):
                continue
            target_height, target_width = len(target), len(target[0])
            matches = 0
            for top in range(len(doubled) - target_height + 1):
                for left in range(len(doubled[0]) - target_width + 1):
                    if all(
                        doubled[top + row][left + col] == target[row][col]
                        for row in range(target_height)
                        for col in range(target_width)
                    ):
                        matches += 1
            if matches:
                shapes.add(
                    (
                        target_height,
                        target_width,
                        bytes(int(cell) for row in target for cell in row),
                    )
                )
                occurrences += matches
        ranked.append(((len(shapes), occurrences), crop))
    best_score = max(score for score, _ in ranked)
    best = [crop for score, crop in ranked if score == best_score]
    if best_score == (0, 0) or len(best) != 1:
        return [row[:] for row in grid]
    return [row[:] for row in best[0]]
