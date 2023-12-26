cost_grid = []
grid = []
with open("input.txt") as file:
    for line in file:
        grid.append([])
        cost_grid.append([])
        for c in line.strip():
            grid[-1].append(c)
            cost_grid[-1].append(0)
start_pos = (grid[-1].index("."), len(grid) - 1)
end_pos = (grid[0].index("."), 0)
print(start_pos)

next_positions = [((start_pos[0], start_pos[1] - 1), [(start_pos[0], start_pos[1])])]
next_next_positions = []
while next_positions:
    (x, y), path = next_positions[-1]
    if grid[y][x + 1] != "#" and (x + 1, y) not in path and cost_grid[y][x + 1] <= len(path) + 1:
        next_path = list(path)
        next_path.append((x + 1, y))
        cost_grid[y][x + 1] = len(next_path)
        if x + 1 != end_pos[0] or y != end_pos[1]:
            next_next_positions.append(((x + 1, y), next_path))

    if grid[y][x - 1] != "#" and (x - 1, y) not in path and cost_grid[y][x - 1] <= len(path) + 1:
        next_path = list(path)
        next_path.append((x - 1, y))
        cost_grid[y][x - 1] = len(next_path)
        if x - 1 != end_pos[0] or y != end_pos[1]:
            next_next_positions.append(((x - 1, y), next_path))

    if grid[y - 1][x] != "#" and (x, y - 1) not in path and cost_grid[y - 1][x] <= len(path) + 1:
        next_path = list(path)
        next_path.append((x, y - 1))
        cost_grid[y - 1][x] = len(next_path)
        if x != end_pos[0] or y - 1 != end_pos[1]:
            next_next_positions.append(((x, y - 1), next_path))

    if y + 1 < len(grid) and grid[y + 1][x] != "#" and (x, y + 1) not in path and cost_grid[y + 1][x] <= len(path) + 1:
        next_path = list(path)
        next_path.append((x, y + 1))
        cost_grid[y + 1][x] = len(next_path)
        if x != end_pos[0] or y + 1 != end_pos[1]:
            next_next_positions.append(((x, y + 1), next_path))

    next_positions.pop(-1)
    next_positions.extend(next_next_positions)
    next_next_positions.clear()
    print("paths", len(next_positions))
    print("cost", cost_grid[end_pos[1]][end_pos[0]] - 1)

print(cost_grid[end_pos[1]][end_pos[0]] - 1)
