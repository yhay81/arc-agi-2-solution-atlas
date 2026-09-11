def solve(grid):
    output = [row[:] for row in grid]
    height, width = len(grid), len(grid[0])
    spine = None
    for r in range(height):
        c = 0
        while c < width:
            if grid[r][c] == 0:
                c += 1
                continue
            start = c
            while c < width and grid[r][c] != 0:
                c += 1
            values = [grid[r][x] for x in range(start, c)]
            if len(values) >= 3 and len(set(values)) == len(values):
                spine = [(r, x) for x in range(start, c)]
                break
        if spine:
            break
    if spine is None:
        for c in range(width):
            r = 0
            while r < height:
                if grid[r][c] == 0:
                    r += 1
                    continue
                start = r
                while r < height and grid[r][c] != 0:
                    r += 1
                values = [grid[x][c] for x in range(start, r)]
                if len(values) >= 3 and len(set(values)) == len(values):
                    spine = [(x, c) for x in range(start, r)]
                    break
            if spine:
                break
    if spine is None:
        return output
    for r, c in spine:
        color = output[r][c]
        for dr, dc in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
            nr, nc = r + dr, c + dc
            while 0 <= nr < height and 0 <= nc < width and output[nr][nc] == 0:
                output[nr][nc] = color
                nr += dr
                nc += dc
    marker_pairs = []
    for r in (0, height - 1):
        for c in range(width - 1):
            if output[r][c] != 0 and output[r][c] == output[r][c + 1]:
                marker_pairs.append((output[r][c], [(r, c), (r, c + 1)]))
    for c in (0, width - 1):
        for r in range(height - 1):
            if output[r][c] != 0 and output[r][c] == output[r + 1][c]:
                marker_pairs.append((output[r][c], [(r, c), (r + 1, c)]))
    for color, seeds in marker_pairs:
        pending = seeds[:]
        seen = set(seeds)
        while pending:
            r, c = pending.pop()
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= nr < height and 0 <= nc < width and output[nr][nc] == 0:
                    output[nr][nc] = color
                    if (nr, nc) not in seen:
                        seen.add((nr, nc))
                        pending.append((nr, nc))
    return output
