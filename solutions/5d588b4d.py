def solve(grid):
    a = grid
    positions = [(r, c) for r, row in enumerate(a) for c, v in enumerate(row) if v]
    if not positions or any(r != 0 for r, c in positions):
        raise ValueError("Expected a single seed run in the first row")
    n = len(positions)
    color = int(a[0][0])
    if [c for r, c in positions] != list(range(n)) or any(v != color for v in a[0][:n]):
        raise ValueError("Expected one contiguous seed color")
    stream = []
    for length in list(range(1, n + 1)) + list(range(n - 1, 0, -1)):
        stream.extend([color] * length + [0])
    width = len(a[0])
    stream.extend([0] * (-len(stream) % width))
    return [stream[i : i + width] for i in range(0, len(stream), width)]
