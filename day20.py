g = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############""".split('\n')

n = len(g)
assert len(g[0]) == n

from itertools import product

def neighbors(nn):
    x, y = nn
    r = set()
    for dx, dy in product([-1, 0, 1], repeat=2):
        if not((dx == 0) ^ (dy == 0)) or not (0 <= x + dx < n) or not (0 <= y + dy < n):
            continue
        if g[x + dx][y + dy] in '.E':
            r.add((x + dx, y + dy))
    return r

def find_pos(ch):
    for i, row in enumerate(g):
        if ch in row:
            return i, row.index(ch)

def distance(start, goal):
    seen = {start}
    frontier =  {start}
    progress = True
    cost = {start: 0}
    while progress:
        progress = False
        new_frontier = set()
        for state in frontier:
            for n in neighbors(state):
                step_cost = 1
                if n in seen and cost[state] + step_cost >= cost[n]:
                    continue
                progress = True
                cost[n] = cost[state] + step_cost
                new_frontier.add(n)
                seen.add(n)
        frontier = new_frontier
    r = cost[goal]
    return r, cost

r = set()
start = find_pos('S')
goal = find_pos('E')

no_cheat_time, from_start = distance(start, goal)
from_end = distance(goal, start)[1]

for i, j in product(range(n), repeat=2):
    if g[i][j] != '#':
        continue
    g[i][j] = '.'
    for nn in neighbors((i, j)):
        x, y = nn
        change = False
        if g[x][y] == '#':
            g[x][y] = '.'
            change = True
            if distance(start, goal)[0] <= no_cheat_time - 100:
                r.add(((i, j), (x, y)))
        if change:
            g[x][y] = '#'
    g[i][j] = '#'

print(len(r))



