def solve(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    for frame in sorted({cell for row in grid for cell in row if cell}):
        positions = [(r, c) for r in range(height) for c in range(width) if grid[r][c] == frame]
        for top, left in positions:
            for bottom, right in positions:
                if bottom - top < 2 or right - left < 2:
                    continue
                perimeter = {(top, c) for c in range(left, right + 1)} | {
                    (bottom, c) for c in range(left, right + 1)
                }
                perimeter |= {(r, left) for r in range(top + 1, bottom)} | {
                    (r, right) for r in range(top + 1, bottom)
                }
                gaps = [(r, c) for r, c in perimeter if grid[r][c] == 0]
                if (
                    len(gaps) != 1
                    or sum(grid[r][c] == frame for r, c in perimeter) != len(perimeter) - 1
                ):
                    continue
                markers = {
                    grid[r][c]
                    for r in range(top + 1, bottom)
                    for c in range(left + 1, right)
                    if grid[r][c] not in (0, frame)
                }
                if len(markers) != 1:
                    continue
                marker = markers.pop()
                if (
                    sum(
                        grid[r][c] == marker
                        for r in range(top + 1, bottom)
                        for c in range(left + 1, right)
                    )
                    != 1
                ):
                    continue
                for r in range(top + 1, bottom):
                    for c in range(left + 1, right):
                        if output[r][c] == 0:
                            output[r][c] = marker
                gap_row, gap_col = gaps[0]
                output[gap_row][gap_col] = marker
                if gap_row == top and top:
                    output[top - 1][left : right + 1] = [marker] * (right - left + 1)
                elif gap_row == bottom and bottom + 1 < height:
                    output[bottom + 1][left : right + 1] = [marker] * (right - left + 1)
                elif gap_col == left and left:
                    for r in range(top, bottom + 1):
                        output[r][left - 1] = marker
                elif gap_col == right and right + 1 < width:
                    for r in range(top, bottom + 1):
                        output[r][right + 1] = marker
    return output
