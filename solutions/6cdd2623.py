def _project_matching_marker_lines(array):
    source = [row[:] for row in array]
    counts = [sum(row.count(v) for row in source) for v in range(10)]
    background = counts.index(max(counts))
    output = [[background] * len(source[0]) for _ in source]
    colors = [value for value in range(10) if value != background and counts[value] == 4]
    for color in colors:
        points = {(r, c) for r, row in enumerate(source) for c, v in enumerate(row) if v == color}
        rows = [
            r
            for r in range(len(source))
            if sum((r, c) in points for c in range(len(source[0]))) >= 2
        ]
        cols = [
            c
            for c in range(len(source[0]))
            if sum((r, c) in points for r in range(len(source))) >= 2
        ]
        for row in rows:
            output[row] = [color] * len(output[0])
        rectangular = bool(rows and cols) and all(
            (row, col) in points for row in rows for col in cols
        )
        if not rectangular:
            for col in cols:
                for row in range(len(output)):
                    output[row][col] = color
    return output


def solve(grid):
    return _project_matching_marker_lines(grid)
