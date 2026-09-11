from dataclasses import dataclass


@dataclass
class Piece:
    color: int
    vertical: set
    horizontal: set
    standalone_bar: bool = False

    @property
    def cells(self):
        return self.vertical | self.horizontal

    def fall(self):
        self.vertical = {(row + 1, col) for row, col in self.vertical}
        self.horizontal = {(row + 1, col) for row, col in self.horizontal}


def _runs(indices):
    groups = []
    for index in indices:
        if not groups or index != groups[-1][-1] + 1:
            groups.append([])
        groups[-1].append(index)
    return groups


def _components(grid, color):
    height, width = len(grid), len(grid[0])
    remaining = {
        (row, col) for row in range(height) for col in range(width) if grid[row][col] == color
    }
    found = []
    while remaining:
        start = min(remaining)
        remaining.remove(start)
        stack = [start]
        cells = set()
        while stack:
            row, col = stack.pop()
            cells.add((row, col))
            for point in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                if point in remaining:
                    remaining.remove(point)
                    stack.append(point)
        found.append(cells)
    return found


def _split_component(cells, color):
    poles = []
    for col in sorted({col for _, col in cells}):
        rows = sorted(row for row, current_col in cells if current_col == col)
        poles.extend(
            Piece(color, {(row, col) for row in run}, set()) for run in _runs(rows) if len(run) >= 2
        )
    used = set().union(*(pole.vertical for pole in poles)) if poles else set()
    pieces = []
    for row in sorted({row for row, _ in cells - used}):
        columns = sorted(col for current_row, col in cells - used if current_row == row)
        for run in _runs(columns):
            bar = {(row, col) for col in run}
            low, high = run[0], run[-1]
            fits = [
                pole
                for pole in poles
                if max(r for r, _ in pole.vertical) == row
                and any((row, col) in pole.vertical for col in (low - 1, high + 1))
            ]
            if fits:
                fits[0].horizontal |= bar
            else:
                pieces.append(Piece(color, set(), bar, standalone_bar=not poles))
    return pieces + poles


def _find_pieces(grid):
    colors = sorted({value for row in grid for value in row} - {0})
    return [
        piece
        for color in colors
        for cells in _components(grid, color)
        for piece in _split_component(cells, color)
    ]


def _join_crossings(pieces):
    for piece in pieces:
        if not piece.vertical:
            continue
        bottom = max(piece.vertical)
        below = bottom[0] + 1, bottom[1]
        if any(
            below in other.horizontal and other.color != piece.color and other.standalone_bar
            for other in pieces
        ):
            piece.vertical.add(below)


def _is_supported(piece, occupied, height):
    if any(
        row >= height - 1 or (row + 1, col) in occupied or (row, col) in occupied
        for row, col in piece.cells
    ):
        return True
    for row in {row for row, _ in piece.cells}:
        columns = sorted(col for current_row, col in piece.cells if current_row == row)
        if any(
            (row, run[0] - 1) in occupied and (row, run[-1] + 1) in occupied
            for run in _runs(columns)
        ):
            return True
    return False


def _settle(pieces, height):
    while True:
        supported = set()
        while True:
            occupied = (
                set().union(*(pieces[index].cells for index in supported)) if supported else set()
            )
            additions = {
                index
                for index, piece in enumerate(pieces)
                if index not in supported and _is_supported(piece, occupied, height)
            }
            if not additions:
                break
            supported |= additions
        if len(supported) == len(pieces):
            return
        for index, piece in enumerate(pieces):
            if index not in supported:
                piece.fall()


def solve(grid):
    keys = set(grid[0]) - {0}
    body = [row[:] for row in grid]
    body[0] = [0] * len(grid[0])
    if not any(value in keys for row in body for value in row):
        return [row[:] for row in grid]

    pieces = _find_pieces(body)
    _join_crossings(pieces)
    pieces = [piece for piece in pieces if piece.color not in keys]
    _settle(pieces, len(grid))

    output = [[0] * len(grid[0]) for _ in grid]
    for field in ("vertical", "horizontal"):
        for piece in pieces:
            for row, col in getattr(piece, field):
                output[row][col] = piece.color
    output[0] = grid[0][:]
    return output
