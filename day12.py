garden = """AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA"""

g = garden.split()
len(g), len(g[0])

def neighbors(p):
    i, j = p
    r = set()
    if i > 0:
        r.add((i - 1, j))
    if i < n - 1:
        r.add((i + 1, j))
    if j > 0:
        r.add((i, j -1))
    if j < n - 1:
        r.add((i, j + 1))
    return r

def side_neighbors(p):
    i, j = p
    if int(i) != i:
        return {(i, j - 1), (i, j + 1)}
    else:
        return {(i - 1, j), (i + 1, j)}

def count_segments(sides):
    r = 0
    seen = set()
    while sides:
        side = list(sides)[0]
        seen.add(side)
        region = {side}
        frontier = {side}
        progress = True
        while progress:
            progress = False
            new_frontier = set()
            for s in frontier:
                sn = side_neighbors(s)
                for neighbor in sn:
                    if neighbor in sides:
                        if neighbor in seen or neighbor in region:
                            continue
                        progress = True
                        region.add(neighbor)
                        seen.add(neighbor)
                        new_frontier.add(neighbor)
            frontier = new_frontier
        r += 1
        sides -= region
    return r


def cloture(area):
    r = 0
    sides = set()
    for p in area:
        if p[0] == 0 or (p[0] - 1, p[1]) not in area:
            sides.add((p[0] - 0.5, p[1]))
        if p[0] == n - 1 or (p[0] + 1, p[1]) not in area:
            sides.add((p[0] + 0.5, p[1]))
        if p[1] == 0 or (p[0], p[1] - 1) not in area:
            sides.add((p[0], p[1] - 0.5))
        if p[1] == n - 1 or (p[0], p[1] + 1) not in area:
            sides.add((p[0], p[1] + 0.5))
    return count_segments(sides)

from itertools import product

seen = set()
n = len(g)
r = 0
while True:
    for i, j in product(range(n), repeat=2):
        if (i, j) not in seen:
            plant = g[i][j]
            region = {(i, j)}
            frontier = {(i, j)}
            seen.add((i, j))
            progress = True
            while progress:
                progress = False
                new_frontier = set()
                for plot in frontier:
                    for neighbor in neighbors(plot):
                        if neighbor in seen or neighbor in region or g[neighbor[0]][neighbor[1]] != plant:
                            continue
                        progress = True
                        region.add(neighbor)
                        seen.add(neighbor)
                        new_frontier.add(neighbor)
                frontier = new_frontier
            break  # from i, j  loop
    area = len(region)
    perimeter = cloture(region)
    print(plant, area, perimeter)
    r += area * perimeter
    if len(seen) >= n ** 2:
        break

print(r)