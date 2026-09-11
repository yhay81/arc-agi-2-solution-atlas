def solve(grid):
    source = [row[:] for row in grid]
    output = [row[:] for row in source]
    height, width = len(source), len(source[0]) if source else 0
    counts = {}
    for row in source:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    if not counts:
        return output
    background = max(counts, key=lambda value: (counts[value], -value))
    groups = [
        [(row, col)]
        for row in range(height)
        for col in range(width)
        if source[row][col] != background
    ]
    while True:
        for first in range(len(groups)):
            merged = False
            for second in range(first):
                joined = set(groups[first]) | set(groups[second])
                row_values = [row for row, _ in joined]
                col_values = [col for _, col in joined]
                close = (
                    min(
                        max(abs(first_row - second_row), abs(first_col - second_col))
                        for first_row, first_col in groups[first]
                        for second_row, second_col in groups[second]
                    )
                    <= 4
                )
                if (
                    max(max(row_values) - min(row_values), max(col_values) - min(col_values)) <= 4
                    and close
                ):
                    groups[second] = list(joined)
                    groups.pop(first)
                    merged = True
                    break
            if merged:
                break
        else:
            break
    templates = []
    seeds = []
    for glyph in groups:
        glyph_counts = {}
        for row, col in glyph:
            value = source[row][col]
            glyph_counts[value] = glyph_counts.get(value, 0) + 1
        if len(glyph_counts) == 2 and min(glyph_counts.values()) == 1:
            base = max(glyph_counts, key=glyph_counts.get)
            marker = min(glyph_counts, key=glyph_counts.get)
            templates.append((base, marker, glyph))
            for row, col in glyph:
                output[row][col] = marker if source[row][col] == base else base
        elif len(glyph) == 1:
            seeds.extend(glyph)
    for row, col in seeds:
        marker = source[row][col]
        for _, template_marker, glyph in templates:
            if template_marker != marker:
                continue
            top = 0 if row < height // 2 else height - 5
            left = 0 if col < width // 2 else width - 5
            minimum_row = min(glyph_row for glyph_row, _ in glyph)
            minimum_col = min(glyph_col for _, glyph_col in glyph)
            for glyph_row, glyph_col in glyph:
                output[glyph_row - minimum_row + top][glyph_col - minimum_col + left] = marker
    return output
