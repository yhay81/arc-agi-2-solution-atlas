def solve(grid):
    if not grid or not grid[0]:
        return [row[:] for row in grid]
    height, width = len(grid), len(grid[0])
    values = sorted({value for row in grid for value in row})
    counts = {value: sum(row.count(value) for row in grid) for value in values}
    background = min(values, key=lambda value: (-counts[value], value))
    if height < 2:
        return [row[:] for row in grid]
    scaffold_candidates = {
        grid[0][col]
        for col in range(width)
        if grid[0][col] != background and grid[0][col] == grid[1][col]
    }
    if not scaffold_candidates:
        return [row[:] for row in grid]
    scaffold = min(scaffold_candidates, key=lambda value: (counts[value], value))
    run_colours = set(values) - {background, scaffold}
    if len(run_colours) != 1:
        return [row[:] for row in grid]
    run_colour = next(iter(run_colours))
    scaffold_columns = [
        col for col in range(width) if grid[0][col] == scaffold or grid[1][col] == scaffold
    ]
    if not scaffold_columns:
        return [row[:] for row in grid]
    scaffolded = [row[:] for row in grid]
    for col in scaffold_columns:
        for row in range(height):
            if grid[row][col] == run_colour:
                break
            if grid[row][col] == background:
                scaffolded[row][col] = scaffold
    runs = []
    for row in range(2, height):
        col = 0
        while col < width:
            if grid[row][col] != run_colour:
                col += 1
                continue
            left = col
            while col + 1 < width and grid[row][col + 1] == run_colour:
                col += 1
            runs.append((row, left, col))
            col += 1
    output = [row[:] for row in scaffolded]
    for row, left, right in runs:
        if not any(
            output[row - 1][col] == scaffold or output[row][col] == scaffold
            for col in range(left, right + 1)
        ):
            continue
        run_length = right - left + 1
        if run_length > 1:
            for col in range(max(0, left - 1), min(width, right + 2)):
                if output[row - 1][col] == background:
                    output[row - 1][col] = scaffold
        elif right + 1 < width and output[row - 1][right + 1] == background:
            output[row - 1][right + 1] = scaffold
        for col in (left - 1, right + 1):
            if 0 <= col < width and output[row][col] == background:
                output[row][col] = scaffold
        if run_length > 1 and left > 0:
            for below in range(row + 1, height):
                if grid[below][left - 1] == run_colour:
                    break
                if output[below][left - 1] == background:
                    output[below][left - 1] = scaffold
        if right + 1 < width:
            for below in range(row + 1, height):
                if grid[below][right + 1] == run_colour:
                    break
                if output[below][right + 1] == background:
                    output[below][right + 1] = scaffold
    return output
