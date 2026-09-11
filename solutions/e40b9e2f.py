def solve(grid):
    height, width = len(grid), len(grid[0])
    cells = [(r, c, grid[r][c]) for r in range(height) for c in range(width) if grid[r][c]]
    candidates = []
    for center_row in range(2 * height - 1):
        for center_col in range(2 * width - 1):
            if (center_row - center_col) % 2:
                continue
            output = [row[:] for row in grid]
            valid = True
            for source_row, source_col, color in cells:
                row, col = source_row, source_col
                for _ in range(3):
                    rotated_row = center_row + 2 * col - center_col
                    rotated_col = center_col - 2 * row + center_row
                    if rotated_row % 2 or rotated_col % 2:
                        valid = False
                        break
                    row, col = rotated_row // 2, rotated_col // 2
                    if not (0 <= row < height and 0 <= col < width) or output[row][col] not in (
                        0,
                        color,
                    ):
                        valid = False
                        break
                    output[row][col] = color
                if not valid:
                    break
            if not valid or output == grid:
                continue
            positions = [(r, c) for r in range(height) for c in range(width) if output[r][c]]
            top, bottom = min(r for r, _ in positions), max(r for r, _ in positions)
            left, right = min(c for _, c in positions), max(c for _, c in positions)
            added = sum(
                not grid[r][c] and output[r][c] for r in range(height) for c in range(width)
            )
            candidates.append((added, (bottom - top + 1) * (right - left + 1), output))
    if not candidates:
        return [row[:] for row in grid]
    score = min((added, area) for added, area, _ in candidates)
    best = [output for added, area, output in candidates if (added, area) == score]
    return best[0] if len(best) == 1 else [row[:] for row in grid]
