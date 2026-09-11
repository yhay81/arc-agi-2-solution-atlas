def _max_count_colors_summary(array):
    colors = sorted({v for row in array for v in row if v != 0})
    if not colors:
        return [row[:] for row in array]
    counts = {color: sum(v == color for row in array for v in row) for color in colors}
    maximum = max(counts.values())
    winners = [color for color in colors if counts[color] == maximum]
    if maximum <= 0:
        return [row[:] for row in array]
    positions = {
        color: [(r, c) for r, row in enumerate(array) for c, v in enumerate(row) if v == color]
        for color in winners
    }
    winners.sort(
        key=lambda color: (
            min(c for _, c in positions[color]),
            min(r for r, _ in positions[color]),
            color,
        )
    )
    return [list(winners) for _ in range(maximum)]


def solve(grid):
    return _max_count_colors_summary(grid)
