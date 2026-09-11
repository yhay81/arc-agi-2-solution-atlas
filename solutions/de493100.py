def solve(grid):
    height, width = len(grid), len(grid[0])
    hidden = 7
    hidden_cells = [
        (row, col) for row in range(height) for col in range(width) if grid[row][col] == hidden
    ]
    top, bottom = min(row for row, _ in hidden_cells), max(row for row, _ in hidden_cells)
    left, right = min(col for _, col in hidden_cells), max(col for _, col in hidden_cells)

    axes = []
    for axis, size in enumerate((height, width)):
        candidates = []
        for center in range(size // 2, 3 * size // 2):
            good = 0
            valid = True
            for row in range(height):
                for col in range(width):
                    mirror_row, mirror_col = (
                        (center - row, col) if axis == 0 else (row, center - col)
                    )
                    if (
                        0 <= mirror_row < height
                        and 0 <= mirror_col < width
                        and grid[row][col] != hidden
                        and grid[mirror_row][mirror_col] != hidden
                    ):
                        if grid[row][col] != grid[mirror_row][mirror_col]:
                            valid = False
                            break
                        good += 1
                if not valid:
                    break
            if valid and good > 50:
                candidates.append((good, center))
        if candidates:
            axes.append((axis, max(candidates)[1]))

    output = [row[:] for row in grid]

    def fill_orbits():
        seen = set()
        for start in hidden_cells:
            if output[start[0]][start[1]] != hidden or start in seen:
                continue
            orbit = {start}
            for axis, center in axes:
                orbit |= {
                    (center - row, col) if axis == 0 else (row, center - col)
                    for row, col in list(orbit)
                }
            orbit = {(row, col) for row, col in orbit if 0 <= row < height and 0 <= col < width}
            seen |= orbit
            values = {output[row][col] for row, col in orbit if output[row][col] != hidden}
            if len(values) == 1:
                value = next(iter(values))
                for row, col in orbit:
                    if output[row][col] == hidden:
                        output[row][col] = value
            elif values:
                raise ValueError("Conflicting reflection donors")

    fill_orbits()
    for row, col in hidden_cells:
        if (
            output[row][col] == hidden
            and col < height
            and row < width
            and output[col][row] != hidden
        ):
            output[row][col] = output[col][row]
    fill_orbits()
    if any(
        output[row][col] == hidden
        for row in range(top, bottom + 1)
        for col in range(left, right + 1)
    ):
        raise ValueError("Unable to reconstruct hidden rectangle")
    return [row[left : right + 1] for row in output[top : bottom + 1]]
