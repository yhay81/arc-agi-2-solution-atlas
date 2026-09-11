from collections import Counter


def solve(grid):
    g = grid
    out = []
    for a in range(0, len(g), 3):
        columns = [c for c in range(len(g[0])) if any(row[c] for row in g[a : a + 2])]
        runs = []
        for c in columns:
            if not runs or c != runs[-1][-1] + 1:
                runs.append([c])
            else:
                runs[-1].append(c)
        blocks = [[row[cs[0] : cs[-1] + 1] for row in g[a : a + 2]] for cs in runs]
        palettes = [frozenset(v for row in p for v in row) for p in blocks]
        common = Counter(palettes).most_common(1)[0][0]
        special = next((j for j, x in enumerate(palettes) if x != common))
        others = [j for j in range(len(blocks)) if j != special]
        matches = []
        for j in others:
            mapping = {}
            okay = True
            for row1, row2 in zip(blocks[j], blocks[special]):
                for x, y in zip(row1, row2):
                    if x in mapping and mapping[x] != y:
                        okay = False
                    mapping[x] = y
            if okay and len(set(mapping.values())) == len(mapping):
                matches.append((j, mapping))
        if len(matches) != 1:
            raise ValueError("color mapping between identical shapes is not unique")
        j, mapping = matches[0]
        odd = next(k for k in others if k != j)
        out.extend([[mapping[v] for v in row] for row in blocks[odd]])
        out.append([0, 0])
    return out[:-1]
