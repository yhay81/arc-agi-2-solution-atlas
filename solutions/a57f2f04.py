from collections import Counter


def solve(grid):
    marker_color = 8
    h, w = len(grid), len(grid[0])
    counts = Counter(value for row in grid for value in row)
    marker = marker_color if marker_color in counts else counts.most_common(1)[0][0]
    seen = set()
    output = [row[:] for row in grid]
    for row in range(h):
        for col in range(w):
            start = (row, col)
            if grid[row][col] == marker or start in seen:
                continue
            stack = [start]
            seen.add(start)
            component = []
            while stack:
                r, c = stack.pop()
                component.append((r, c))
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < h
                        and 0 <= nc < w
                        and grid[nr][nc] != marker
                        and (nr, nc) not in seen
                    ):
                        seen.add((nr, nc))
                        stack.append((nr, nc))
            top, bottom = min(r for r, _ in component), max(r for r, _ in component)
            left, right = min(c for _, c in component), max(c for _, c in component)
            block = [line[left : right + 1] for line in grid[top : bottom + 1]]
            nonzero = [
                (r, c) for r in range(len(block)) for c in range(len(block[0])) if block[r][c] != 0
            ]
            if not nonzero:
                continue
            mt, ml = min(r for r, _ in nonzero), min(c for _, c in nonzero)
            mb, mr = max(r for r, _ in nonzero), max(c for _, c in nonzero)
            motif = [line[ml : mr + 1] for line in block[mt : mb + 1]]
            mh, mw = len(motif), len(motif[0])
            bh, bw = len(block), len(block[0])
            if bh % mh or bw % mw:
                continue
            for r in range(bh):
                for c in range(bw):
                    output[top + r][left + c] = motif[r % mh][c % mw]
    return output
