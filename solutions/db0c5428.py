from collections import Counter


def solve(grid):
    height, width = len(grid), len(grid[0])
    counts = Counter(value for row in grid for value in row)
    background = min((value for value, count in counts.items() if count == max(counts.values())))
    positions = [(r, c) for r in range(height) for c in range(width) if grid[r][c] != background]
    if not positions:
        return [row[:] for row in grid]
    top, left = min(r for r, _ in positions), min(c for _, c in positions)
    bottom, right = max(r for r, _ in positions), max(c for _, c in positions)
    if (bottom - top + 1, right - left + 1) != (9, 9):
        return [row[:] for row in grid]
    source = [row[left : left + 9] for row in grid[top : top + 9]]
    if any(source[r][c] != background for r in range(3, 6) for c in range(3, 6)):
        return [row[:] for row in grid]
    block_map: tuple[tuple[int | None, ...], ...] = (
        (8, None, 7, None, 6),
        (None, 0, 1, 2, None),
        (5, 3, None, 5, 3),
        (None, 6, 7, 8, None),
        (2, None, 1, None, 0),
    )
    expanded = [[background] * 15 for _ in range(15)]
    for macro_row, row in enumerate(block_map):
        for macro_col, source_index in enumerate(row):
            if source_index is None:
                continue
            source_row, source_col = divmod(source_index, 3)
            for dr in range(3):
                for dc in range(3):
                    expanded[macro_row * 3 + dr][macro_col * 3 + dc] = source[source_row * 3 + dr][
                        source_col * 3 + dc
                    ]
    non_background = [value for row in source for value in row if value != background]
    if not len(non_background):
        return [row[:] for row in grid]
    object_counts = Counter(non_background)
    object_color = min(
        (value for value, count in object_counts.items() if count == max(object_counts.values()))
    )
    centre = [[source[r][c] for c in (2, 4, 6)] for r in (2, 4, 6)]
    centre[1][1] = object_color
    for r in range(3):
        for c in range(3):
            expanded[6 + r][6 + c] = centre[r][c]
    expanded_top, expanded_left = top - 3, left - 3
    if (
        expanded_top < 0
        or expanded_left < 0
        or expanded_top + 15 > height
        or expanded_left + 15 > width
    ):
        return [row[:] for row in grid]
    output = [[background] * width for _ in range(height)]
    for r in range(15):
        for c in range(15):
            output[expanded_top + r][expanded_left + c] = expanded[r][c]
    return output
