grid = [*open('day24/input.txt')]
h, w = len(grid)-2, len(grid[0].strip())-2
wrap = lambda p: complex(p.real%w, p.imag%h)
dirs = {'x': 0, '<':-1, '>':+1, '^':-1j,'v':+1j}
bliz = {d: {complex(x, y) for x in range(w) for y in range(h)
                            if grid[y+1][x+1]==d} for d in dirs}

home, goal = complex(0, -1), complex(w-1, h)
todo, time, trip = [home], 0, 0

while todo:
    bliz = {d: {wrap(p+dirs[d]) for p in bliz[d]} for d in dirs}
    curr = {p+dirs[d] for p in todo for d in dirs}
    todo, time = [], time + 1

    for pos in curr:
        if (trip, pos) in ((0, goal), (1, home), (2, goal)):
            if trip == 0: print(time)
            if trip == 2: print(time); exit()
            todo, trip = [pos], trip + 1; break

        if all((pos not in bliz[d] for d in bliz)) and pos==wrap(pos) or pos in (home, goal):
            todo += [pos]