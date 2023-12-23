grid = []
with open("input.txt") as file:
    for line in file:
        grid.append([])
        for c in line.strip():
            grid[-1].append(c)

start_position = ()
for y in range(len(grid)):
    for x in range(len(grid)):
        if grid[y][x] == "S":
            start_position = ((x, y), (0, 0))

current_positions = set()
current_positions.add(start_position)
next_positions = set()
for _ in range(26501365):
    print(len(current_positions))
    for (x, y), (mx, my) in current_positions:
        if x + 1 < len(grid[y]) and grid[y][x + 1] != "#":
            next_positions.add(((x + 1, y), (mx, my)))

        if x - 1 >= 0 and grid[y][x - 1] != "#":
            next_positions.add(((x - 1, y), (mx, my)))

        if y + 1 < len(grid) and grid[y + 1][x] != "#":
            next_positions.add(((x, y + 1), (mx, my)))

        if y - 1 >= 0 and grid[y - 1][x] != "#":
            next_positions.add(((x, y - 1), (mx, my)))

        if x + 1 == len(grid[y]) and grid[y][0] != "#":
            next_positions.add(((0, y), (mx, my)))

        if x - 1 == -1 and grid[y][len(grid[y])-1] != "#":
            next_positions.add(((len(grid[y])-1, y), (mx, my)))

        if y + 1 == len(grid) and grid[0][x] != "#":
            next_positions.add(((x, 0), (mx, my)))

        if y - 1 == -1 and grid[len(grid)-1][x] != "#":
            next_positions.add(((x, len(grid)-1), (mx, my)))

    current_positions.clear()
    current_positions = set(next_positions)
    next_positions.clear()
print(len(current_positions))
