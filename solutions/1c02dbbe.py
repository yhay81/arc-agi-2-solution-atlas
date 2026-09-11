def where(grid, color):
    ps = [(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == color]
    return ([r for r, _ in ps], [c for _, c in ps])


def solve(grid):
    grid = [row[:] for row in grid]
    taskvars = {"object_color": 5}
    object_color = taskvars["object_color"]
    output_grid = [row[:] for row in grid]
    object_cells = where(grid, object_color)
    if len(object_cells[0]) == 0:
        return output_grid
    rect_top = min(object_cells[0])
    rect_bottom = max(object_cells[0])
    rect_left = min(object_cells[1])
    rect_right = max(object_cells[1])
    unique_colors = {v for row in grid for v in row}
    marker_colors = [c for c in unique_colors if c != 0 and c != object_color]
    external_markers_to_remove = []
    for color in marker_colors:
        marker_cells = where(grid, color)
        if len(marker_cells[0]) != 3:
            continue
        marker_positions = list(zip(marker_cells[0], marker_cells[1]))
        corner_pos = None
        external_markers = []
        for pos in marker_positions:
            r, c = pos
            if rect_top <= r <= rect_bottom and rect_left <= c <= rect_right:
                corner_pos = pos
            else:
                external_markers.append(pos)
        if corner_pos is None or len(external_markers) != 2:
            continue
        external_markers_to_remove.extend(external_markers)
        corner_r, corner_c = corner_pos
        if corner_r == rect_top and corner_c == rect_left:
            width_marker = None
            height_marker = None
            for r, c in external_markers:
                if r == rect_top - 1:
                    width_marker = (r, c)
                elif c == rect_left - 1:
                    height_marker = (r, c)
            if width_marker and height_marker:
                width = width_marker[1] - rect_left + 1
                height = height_marker[0] - rect_top + 1
                for r in range(rect_top, rect_top + height):
                    for c in range(rect_left, rect_left + width):
                        if rect_top <= r <= rect_bottom and rect_left <= c <= rect_right:
                            output_grid[r][c] = color
        elif corner_r == rect_top and corner_c == rect_right:
            width_marker = None
            height_marker = None
            for r, c in external_markers:
                if r == rect_top - 1:
                    width_marker = (r, c)
                elif c == rect_right + 1:
                    height_marker = (r, c)
            if width_marker and height_marker:
                width = rect_right - width_marker[1] + 1
                height = height_marker[0] - rect_top + 1
                for r in range(rect_top, rect_top + height):
                    for c in range(rect_right - width + 1, rect_right + 1):
                        if rect_top <= r <= rect_bottom and rect_left <= c <= rect_right:
                            output_grid[r][c] = color
        elif corner_r == rect_bottom and corner_c == rect_left:
            width_marker = None
            height_marker = None
            for r, c in external_markers:
                if r == rect_bottom + 1:
                    width_marker = (r, c)
                elif c == rect_left - 1:
                    height_marker = (r, c)
            if width_marker and height_marker:
                width = width_marker[1] - rect_left + 1
                height = rect_bottom - height_marker[0] + 1
                for r in range(rect_bottom - height + 1, rect_bottom + 1):
                    for c in range(rect_left, rect_left + width):
                        if rect_top <= r <= rect_bottom and rect_left <= c <= rect_right:
                            output_grid[r][c] = color
        else:
            width_marker = None
            height_marker = None
            for r, c in external_markers:
                if r == rect_bottom + 1:
                    width_marker = (r, c)
                elif c == rect_right + 1:
                    height_marker = (r, c)
            if width_marker and height_marker:
                width = rect_right - width_marker[1] + 1
                height = rect_bottom - height_marker[0] + 1
                for r in range(rect_bottom - height + 1, rect_bottom + 1):
                    for c in range(rect_right - width + 1, rect_right + 1):
                        if rect_top <= r <= rect_bottom and rect_left <= c <= rect_right:
                            output_grid[r][c] = color
    for r, c in external_markers_to_remove:
        output_grid[r][c] = 0
    return output_grid
