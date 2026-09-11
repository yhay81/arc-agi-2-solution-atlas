def solve(grid):
    h, w = len(grid), len(grid[0])
    slots = {}
    slot_by_missing = {(1, 1): (0, 0), (1, 0): (0, 2), (0, 1): (2, 0), (0, 0): (2, 2)}
    for color in sorted({value for row in grid for value in row if value}):
        if color == 0:
            continue
        seen = set()
        for r in range(h):
            for c in range(w):
                if grid[r][c] != color or (r, c) in seen:
                    continue
                stack = [(r, c)]
                seen.add((r, c))
                component = []
                while stack:
                    cr, cc = stack.pop()
                    component.append((cr, cc))
                    for nr, nc in ((cr - 1, cc), (cr + 1, cc), (cr, cc - 1), (cr, cc + 1)):
                        if (
                            0 <= nr < h
                            and 0 <= nc < w
                            and grid[nr][nc] == color
                            and (nr, nc) not in seen
                        ):
                            seen.add((nr, nc))
                            stack.append((nr, nc))
                rows = [row for row, _ in component]
                cols = [col for _, col in component]
                top, left = (min(rows), min(cols))
                shape = [row[left : max(cols) + 1] for row in grid[top : max(rows) + 1]]
                if (
                    len(shape) != 2
                    or len(shape[0]) != 2
                    or sum(value != 0 for row in shape for value in row) != 3
                ):
                    continue
                missing = next((r, c) for r in range(2) for c in range(2) if shape[r][c] == 0)
                slots[slot_by_missing[missing]] = shape
    if len(slots) != 4:
        return [row[:] for row in grid]
    output = [[0] * 4 for _ in range(4)]
    for (row, col), shape in slots.items():
        for dr in range(2):
            for dc in range(2):
                output[row + dr][col + dc] = shape[dr][dc]
    return output
