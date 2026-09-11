def solve(grid):
    h, w = len(grid), len(grid[0])
    observed = {}
    for row in range(h):
        for col in range(w):
            center = grid[row][col]
            if not center:
                continue
            by_color = {}
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if not (dr or dc) or not (0 <= row + dr < h and 0 <= col + dc < w):
                        continue
                    neighbor = grid[row + dr][col + dc]
                    if neighbor and neighbor != center:
                        by_color.setdefault(neighbor, set()).add((dr, dc))
            for shell, offsets in by_color.items():
                if len(offsets) >= 2 and {(-dr, -dc) for dr, dc in offsets} == offsets:
                    observed.setdefault(center, set()).add((shell, frozenset(offsets)))
    templates = {}
    for center, candidates in observed.items():
        largest = max(len(offsets) for _, offsets in candidates)
        best = [candidate for candidate in candidates if len(candidate[1]) == largest]
        if len(best) == 1:
            templates[center] = best[0]
    if not templates:
        return [row[:] for row in grid]
    output = [row[:] for row in grid]
    for center, (shell, offsets) in templates.items():
        for row in range(h):
            for col in range(w):
                if grid[row][col] == center:
                    cells = [(row + dr, col + dc) for dr, dc in offsets]
                    if all(
                        0 <= r < h and 0 <= c < w and grid[r][c] in (0, shell) for r, c in cells
                    ):
                        for r, c in cells:
                            output[r][c] = shell
        for row in range(h):
            for col in range(w):
                if grid[row][col] != 0:
                    continue
                cells = [(row + dr, col + dc) for dr, dc in offsets]
                if all(0 <= r < h and 0 <= c < w and grid[r][c] == shell for r, c in cells):
                    output[row][col] = center
    return output
