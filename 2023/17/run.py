import sys


class Path:
    def __init__(self):
        self.current_node = None
        self.d = None
        self.path = ""
        self.heat = 0


grid = []
with open("input.txt") as file:
    for line in file:
        grid.append([])
        for d in line.strip():
            grid[-1].append(int(d))
start_path = Path()
start_path.current_node = (0, 0)
start_path.path = ""
start_path.heat = 0

min_heat = {}
for y in range(len(grid)):
    for x in range(len(grid[0])):
        for d in "RLDU":
            for i in range(1, 4):
                min_heat[(x, y, d, i)] = [sys.maxsize, None]

paths = [start_path]
next_paths = []
current_pos = (0, 0)
count = 0
while paths:
    count += 1
    for path in paths:
        px, py = path.current_node

        for move in [(1, 0, "R"), (-1, 0, "L"), (0, 1, "D"), (0, -1, "U")]:
            dx, dy, d = move
            x = px + dx
            y = py + dy

            if x < 0 or y < 0 or x > len(grid[0]) - 1 or y > len(grid) - 1:
                continue

            if path.path[-3:] + d in ["RRRR", "DDDD", "UUUU", "LLLL"]:
                continue

            n_step = 1
            if len(path.path) > 0 and path.path[-1] == d:
                n_step = 2
                if len(path.path) > 1 and path.path[-2] == d:
                    n_step = 3

            next_heat = path.heat + grid[y][x]
            if min_heat[(x, y, d, n_step)][0] < next_heat:
                continue
            else:
                next_path = Path()
                next_path.current_node = (x, y)
                next_path.dir = d
                next_path.path = path.path + d
                next_path.heat = next_heat

                next_paths.append(next_path)

                min_heat[(x, y, d, n_step)][0] = next_heat
                min_heat[(x, y, d, n_step)][1] = next_path

    paths.clear()
    paths.extend(next_paths)
    print(count, len(paths))
    next_paths.clear()

min_end_heat = sys.maxsize
min_end_path = None
for key in min_heat.keys():
    if key[0] == 12 and key[1] == 12:
        if min_end_heat > min_heat[key][0]:
            min_end_heat, min_end_path = min_heat[key]

print(min_end_path.path)
print(min_end_heat)
