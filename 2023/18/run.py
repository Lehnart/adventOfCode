digs = set()
digs.add((0, 0))
current_pos = (0, 0)
direction_move = {"U": (0, -1), "R": (1, 0), "D": (0, 1), "L": (-1, 0)}

with open("input.txt") as file:
    for line in file:
        direction, raw_count, _ = line.split()
        count = int(raw_count)
        dx, dy = direction_move[direction]
        for _ in range(count):
            current_pos = (current_pos[0] + dx, current_pos[1] + dy)
            digs.add(current_pos)

with open("output.txt", "w") as file:
    min_x = min(p[0] for p in digs)
    max_x = max(p[0] for p in digs)
    min_y = min(p[1] for p in digs)
    max_y = max(p[1] for p in digs)
    print(min_x, max_x, min_y, max_y)
    for j in range(0, max_y - min_y + 1):
        for i in range(0, max_x - min_x + 1):
            pos = (i + min_x, j + min_y)
            if pos in digs:
                file.write("#")
            else:
                file.write(".")
        file.write("\n")

grid = []
with open("output.txt") as file:
    for line in file:
        grid.append([])
        for c in line.strip():
            grid[-1].append(c)

visited_nodes = set()
visited_nodes.add((69, 0))

step = 0
nodes_to_visit = [(70, 0)]
nodes_left = []
nodes_right = []
next_nodes_to_visit = []

while nodes_to_visit:

    for x, y in nodes_to_visit:
        visited_nodes.add((x, y))

        if (x + 1, y) not in visited_nodes and x + 1 <= len(grid[0]) - 1 and grid[y][x + 1] == "#":
            next_nodes_to_visit.append((x + 1, y))
            nodes_left.append((x + 1, y - 1))
            nodes_right.append((x + 1, y + 1))
            nodes_left.append((x, y - 1))
            nodes_right.append((x, y + 1))
        elif (x - 1, y) not in visited_nodes and x - 1 >= 0 and grid[y][x - 1] == "#":
            next_nodes_to_visit.append((x - 1, y))
            nodes_left.append((x - 1, y + 1))
            nodes_right.append((x - 1, y - 1))
            nodes_left.append((x, y + 1))
            nodes_right.append((x, y - 1))
        elif (x, y - 1) not in visited_nodes and y - 1 >= 0 and grid[y - 1][x] == "#":
            next_nodes_to_visit.append((x, y - 1))
            nodes_left.append((x - 1, y - 1))
            nodes_right.append((x + 1, y - 1))
            nodes_left.append((x - 1, y))
            nodes_right.append((x + 1, y))
        elif (x, y + 1) not in visited_nodes and y + 1 <= len(grid) - 1 and grid[y + 1][x] == "#":
            next_nodes_to_visit.append((x, y + 1))
            nodes_left.append((x + 1, y + 1))
            nodes_right.append((x - 1, y + 1))
            nodes_left.append((x + 1, y))
            nodes_right.append((x - 1, y))
        nodes_to_visit.clear()
        nodes_to_visit.extend(next_nodes_to_visit)
        next_nodes_to_visit.clear()

new_nodes_right = set()
for node in nodes_right :
    if node not in visited_nodes :
        new_nodes_right.add(node)
nodes_right = new_nodes_right

for y in range(0, len(grid)):
    for x in range(0, len(grid[0])):
        if (x, y) in nodes_right and (x, y):
            print("R", end="")
        else:
            print(".", end="")
    print()


nodes_right = set(nodes_right)
inside_nodes = set()
is_inside = False
for y in range(0, len(grid)):
    for x in range(0, len(grid[0])):
        if (x - 1, y) in nodes_right and (x, y) not in visited_nodes:
            nodes_right.add((x, y))
        elif (x, y) in nodes_right:
            nodes_right.add((x, y))

union = visited_nodes.union(nodes_right)
for y in range(0, len(grid)):
    for x in range(0, len(grid[0])):
        if (x, y) in union and (x, y):
            print("R", end="")
        else:
            print(".", end="")
    print()


print(len(visited_nodes.union(nodes_right)))
