universe = []
with open("input.txt") as file:
    for line in file:
        universe.append(line.strip())

row_without_star = []
col_without_star = []
for row_index, row in enumerate(universe):
    if "#" not in row:
        row_without_star.append(row_index
                                )
for col_index in range(len(universe[0])):
    col = [r[col_index] for r in universe]
    if "#" not in col:
        col_without_star.append(col_index)

galaxies = []
for y in range(len(universe)):
    for x in range(len(universe[0])):
        if universe[y][x] == "#":
            galaxies.append([x,y])

for galaxy in galaxies :
    x,y  = galaxy
    dx, dy = (0,0)
    for x0 in col_without_star :
        if x0 < x :
            dx += 999999
    for y0 in row_without_star :
        if y0 < y :
            dy += 999999
    galaxy[0] = x + dx
    galaxy[1] = y + dy
steps = 0
for i in range(len(galaxies)):
    for j in range(i , len(galaxies)):
        steps += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
print(steps)