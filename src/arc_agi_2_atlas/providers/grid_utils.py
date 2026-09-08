import numpy as np


def group_connected_positions(positions, connectivity=8):
    """
    Group positions into connected components.

    Parameters:
    positions    : list or ndarray of shape (n, 2) → [[row, col], ...]
    connectivity : 4 or 8 (neighbor definition)

    Returns:
    list of lists of positions (connected components)
    """
    positions = np.array(positions)
    visited = set()
    groups = []

    # Neighbor offsets
    if connectivity == 4:
        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    elif connectivity == 8:
        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    else:
        raise ValueError("Connectivity must be 4 or 8")

    pos_set = set(map(tuple, positions))

    for pos in pos_set:
        if pos not in visited:
            group = []
            stack = [pos]
            visited.add(pos)
            while stack:
                r, c = stack.pop()
                group.append([r, c])
                for dr, dc in neighbors:
                    nbr = (r + dr, c + dc)
                    if nbr in pos_set and nbr not in visited:
                        visited.add(nbr)
                        stack.append(nbr)
            groups.append(group)

    return groups


def find_min_square_tile(grid):
    """
    Find the smallest square non-zero block that can generate the entire input
    (excluding the rectangle with 0s) by tiling left-to-right and top-to-bottom.
    """
    grid = np.array(grid)
    nrows, ncols = grid.shape

    # Locate the zero block bounds
    zero_rows, zero_cols = np.where(grid == 0)
    if zero_rows.size > 0:
        rmin, rmax = zero_rows.min(), zero_rows.max() + 1
        cmin, cmax = zero_cols.min(), zero_cols.max() + 1
    else:
        rmin, rmax, cmin, cmax = nrows, nrows, ncols, ncols  # no zeros

    # Mask out the zero block
    mask = np.ones_like(grid, dtype=bool)
    mask[rmin:rmax, cmin:cmax] = False

    # Search for the minimal square size
    max_tile_size = min(nrows, ncols)
    for size in range(1, max_tile_size + 1):
        # Candidate tile: take from top-left non-zero region
        tile = grid[0:size, 0:size]

        if np.any(tile == 0):
            continue  # tile must be non-zero

        # Build complete tiled grid of input size
        reps_row = -(-nrows // size)  # ceil division
        reps_col = -(-ncols // size)
        tiled = np.tile(tile, (reps_row, reps_col))[:nrows, :ncols]

        # Compare only where mask is True (ignore 0-block)
        if np.all(tiled[mask] == grid[mask]):
            return tile, tiled

    return None, None  # no valid tile found


def move_parts(parts, direction, output_grid, input_grid):
    nrows, ncols = output_grid.shape
    markers = []
    for part in parts:
        if direction == "left to right":
            markers.append(part[:, 1].max())
        elif direction == "right to left":
            markers.append(part[:, 1].min())
        elif direction == "top to bottom":
            markers.append(part[:, 0].max())
        elif direction == "bottom to top":
            markers.append(part[:, 0].min())

    # Order blocks for movement
    if direction in ["left to right", "top to bottom"]:
        order = np.argsort(markers)[::-1]
    else:
        order = np.argsort(markers)

    for i in order:
        part = parts[i]
        min_row, min_col = part.min(axis=0)
        max_row, max_col = part.max(axis=0)
        mark = markers[i]

        if direction == "left to right":
            if mark == ncols - 1:
                continue
            final_shift = 0  # Compute maximum feasible shift
            for shift in range(1, ncols):
                if (
                    max_col + shift >= ncols
                    or output_grid[min_row : max_row + 1, max_col + shift].any() != 0
                ):  # Check for collisions
                    break
                final_shift += 1
            for r, c in part:  # Apply the shift
                output_grid[r, c] = 0
                output_grid[r, c + final_shift] = input_grid[r, c]
        elif direction == "right to left":
            if mark == 0:
                continue
            final_shift = 0
            for shift in range(1, ncols):
                if (
                    min_col - shift < 0
                    or output_grid[min_row : max_row + 1, min_col - shift].any() != 0
                ):
                    break
                final_shift += 1
            for r, c in part:
                output_grid[r, c] = 0
                output_grid[r, c - final_shift] = input_grid[r, c]
        elif direction == "top to bottom":
            if mark == nrows - 1:
                continue
            final_shift = 0
            for shift in range(1, nrows):
                if (
                    max_row + shift >= nrows
                    or output_grid[max_row + shift, min_col : max_col + 1].any() != 0
                ):
                    break
                final_shift += 1
            for r, c in part:
                output_grid[r, c] = 0
                output_grid[r + final_shift, c] = input_grid[r, c]
        elif direction == "bottom to top":
            if mark == 0:
                continue
            final_shift = 0
            for shift in range(1, nrows):
                if (
                    min_row - shift < 0
                    or output_grid[min_row - shift, min_col : max_col + 1].any() != 0
                ):
                    break
                final_shift += 1
            for r, c in part:
                output_grid[r, c] = 0
                output_grid[r - final_shift, c] = input_grid[r, c]
    return output_grid


def is_straight_line(positions):
    """
    Check if a group of positions form a straight line on a grid.

    Args:
        positions: List of (row, col) tuples representing positions on a grid

    Returns:
        tuple: (is_line, endpoints)
            - is_line: True if positions form a straight line
            - endpoints: List of two endpoint positions if is_line is True, None otherwise
    """
    # Handle trivial cases
    if len(positions) < 2:
        return True, positions

    positions = np.array(positions)

    # Check for horizontal line (all points have same row)
    if np.all(positions[:, 0] == positions[0, 0]):
        # Sort by column to get endpoints
        sorted_by_col = positions[positions[:, 1].argsort()]
        return True, [sorted_by_col[0], sorted_by_col[-1]]

    # Check for vertical line (all points have same column)
    if np.all(positions[:, 1] == positions[0, 1]):
        # Sort by row to get endpoints
        sorted_by_row = positions[positions[:, 0].argsort()]
        return True, [sorted_by_row[0], sorted_by_row[-1]]

    # Check for diagonal line by verifying consistent slope
    p1 = positions[0]
    p2 = positions[1]

    # Handle vertical slope case
    if p2[1] == p1[1]:
        return False, None

    reference_slope = (p2[0] - p1[0]) / (p2[1] - p1[1])

    # Check if all points have the same slope relative to first point
    for i in range(2, len(positions)):
        current_point = positions[i]

        # Handle potential division by zero
        if current_point[1] == p1[1]:
            return False, None

        current_slope = (current_point[0] - p1[0]) / (current_point[1] - p1[1])

        # Check slope equality with small tolerance for floating point precision
        if abs(current_slope - reference_slope) > 1e-10:
            return False, None

    # For diagonal lines, sort by row to get endpoints
    sorted_by_row = positions[positions[:, 0].argsort()]
    endpoints = [sorted_by_row[0], sorted_by_row[-1]]
    return True, endpoints


def connect_points_with_lines(grid, points, value):
    """
    Connect all points with straight lines on a grid (fully connected graph).

    Args:
        grid: 2D numpy array representing the grid
        points: List of (row, col) tuples representing points to connect
        value: Value to set along the lines

    Returns:
        2D numpy array with the lines drawn
    """

    def draw_line(grid, start, end, value):
        """
        Draw a straight line between two points using Bresenham's algorithm.

        Args:
            grid: 2D numpy array representing the grid
            start: Tuple (row, col) for the starting point
            end: Tuple (row, col) for the ending point
            value: Value to set along the line

        Returns:
            2D numpy array with the line drawn
        """
        result_grid = grid.copy()

        # Extract coordinates
        y0, x0 = start
        y1, x1 = end

        # Determine if the line is steep (more vertical than horizontal)
        steep = abs(y1 - y0) > abs(x1 - x0)

        # If line is steep, transpose coordinates
        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1

        # If line goes from right to left, swap endpoints
        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        # Calculate deltas and error
        dx = x1 - x0
        dy = abs(y1 - y0)
        error = dx // 2  # Integer division for handling pixel centers

        # Determine y step direction
        y = y0
        y_step = 1 if y0 < y1 else -1

        # Draw the line pixel by pixel
        for x in range(x0, x1 + 1):
            # Plot point based on steepness
            if steep:
                if 0 <= y < result_grid.shape[1] and 0 <= x < result_grid.shape[0]:
                    result_grid[x, y] = value
            else:
                if 0 <= y < result_grid.shape[0] and 0 <= x < result_grid.shape[1]:
                    result_grid[y, x] = value

            # Update error and y coordinate
            error -= dy
            if error < 0:
                y += y_step
                error += dx

        return result_grid

    if len(points) < 2:
        return grid

    result = grid.copy()

    # Draw lines between each pair of points (fully connected)
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            start = points[i]
            end = points[j]
            result = draw_line(result, start, end, value)

    return result


def extract_min_bound_block(grid, positions):
    """
    Extract the minimal bounding block from the grid that contains all specified positions.

    Args:
        grid (np.ndarray): The input grid.
        positions (array-like): List or array of (row, col) positions.

    Returns:
        np.ndarray: The extracted block as a subarray of the grid.
    """
    grid = np.array(grid)
    positions = np.array(positions)
    min_row, min_col = positions.min(axis=0)
    max_row, max_col = positions.max(axis=0)
    block = grid[min_row : max_row + 1, min_col : max_col + 1]
    return block
