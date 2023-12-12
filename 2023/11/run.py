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

for row_index in row_without_star[::-1]:
    universe.insert(row_index, "".join(["." for _ in range(len(universe[0]))]))
for col_index in col_without_star[::-1]:
    for row_index in range(len(universe)):
        row = universe[row_index]
        universe[row_index] = row[:col_index] + "." + row[col_index:]

galaxies = []
for y in range(len(universe)):
    for x in range(len(universe[0])):
        if universe[y][x] == "#":
            galaxies.append((x,y))

steps = 0
for i in range(len(galaxies)):
    for j in range(i , len(galaxies)):
        steps += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
print(steps)