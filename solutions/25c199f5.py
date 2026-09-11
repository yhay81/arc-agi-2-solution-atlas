from collections import Counter


def solve(grid):
    return_trace = False
    grid = [row[:] for row in grid]
    h, w = (len(grid), len(grid[0]))
    if (w - 2) % 3:
        raise ValueError("Expected three equally wide panels and two separators")
    width = (w - 2) // 3
    separators = (width, 2 * width + 1)
    sep_colors = {grid[r][c] for r in range(h) for c in separators}
    if len(sep_colors) != 1:
        raise ValueError("Panel separators are not uniform")
    panels = [[row[i * (width + 1) : i * (width + 1) + width] for row in grid] for i in range(3)]
    background = Counter(v for panel in panels for row in panel for v in row).most_common(1)[0][0]
    if background in sep_colors:
        raise ValueError("Separator cannot be the panel background")
    out = [[background] * width for _ in range(h)]
    bottom = h
    trace = []
    for i, panel in enumerate(panels):
        occupied_rows = [r for r, row in enumerate(panel) if any(v != background for v in row)]
        if not occupied_rows:
            raise ValueError("Empty panel rule has not been verified")
        top, last = (min(occupied_rows), max(occupied_rows))
        height = last - top + 1
        bottom -= height
        if bottom < 0:
            raise ValueError("Stack exceeds the panel height")
        for offset, row in enumerate(panel[top : last + 1]):
            out[bottom + offset] = row[:]
        trace.append(
            dict(
                panel=i + 1,
                source_rows=[top, last],
                destination_rows=[bottom, bottom + height - 1],
                vertical_shift=bottom - top,
            )
        )
    return (
        (out, dict(background=background, panel_width=width, placements=trace))
        if return_trace
        else out
    )
