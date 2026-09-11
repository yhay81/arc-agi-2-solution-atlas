def solve(grid):
    height, width = len(grid), len(grid[0])
    frame, fill = 5, 8
    positions = [(r, c) for r in range(height) for c in range(width) if grid[r][c] == frame]
    if len(positions) < 8:
        return [row[:] for row in grid]
    top, bottom = min(r for r, _ in positions), max(r for r, _ in positions)
    left, right = min(c for _, c in positions), max(c for _, c in positions)
    perimeter = {(top, c) for c in range(left, right + 1)} | {
        (bottom, c) for c in range(left, right + 1)
    }
    perimeter |= {(r, left) for r in range(top + 1, bottom)} | {
        (r, right) for r in range(top + 1, bottom)
    }
    gaps = [(r, c) for r, c in perimeter if grid[r][c] != frame]
    if bottom - top < 2 or right - left < 2 or len(gaps) != 1 or grid[gaps[0][0]][gaps[0][1]]:
        return [row[:] for row in grid]
    output = [row[:] for row in grid]
    for r in range(top + 1, bottom):
        for c in range(left + 1, right):
            if not output[r][c]:
                output[r][c] = fill
    gap_row, gap_col = gaps[0]
    if gap_row == top:
        for r in range(top - 1, -1, -1):
            if not output[r][gap_col]:
                output[r][gap_col] = fill
    elif gap_row == bottom:
        for r in range(bottom + 1, height):
            if not output[r][gap_col]:
                output[r][gap_col] = fill
    elif gap_col == left:
        for c in range(left - 1, -1, -1):
            if not output[gap_row][c]:
                output[gap_row][c] = fill
    elif gap_col == right:
        for c in range(right + 1, width):
            if not output[gap_row][c]:
                output[gap_row][c] = fill
    else:
        return [row[:] for row in grid]
    output[gap_row][gap_col] = fill
    return output
