def move_north(grid):
    next_grid = []
    for row_index, line in enumerate(grid):
        next_grid.append("")
        for c_index, c in enumerate(line):
            if c in ".#":
                next_grid[-1] += c
            elif c == "O":
                j = row_index - 1
                while j >= 0 and next_grid[j][c_index] == ".":
                    j -= 1
                next_grid[j + 1] = next_grid[j + 1][:c_index] + "O" + next_grid[j + 1][c_index + 1:]
                if j != row_index - 1:
                    next_grid[row_index] = next_grid[row_index][:c_index] + "." + next_grid[row_index][c_index + 1:]
            else:
                raise Exception
    return next_grid


def move_south(grid):
    grid = grid[::-1]
    next_grid = move_north(grid)
    return next_grid[::-1]


def move_east(grid):
    rotated_grid = []
    for col_index in range(len(grid)):
        col = "".join([row[col_index] for row in grid])
        rotated_grid.append(col)

    unrotated_next_grid = []
    next_grid = move_north(rotated_grid[::-1])
    for col_index in range(len(next_grid)):
        col = "".join([row[col_index] for row in next_grid])
        unrotated_next_grid.append(col[::-1])

    return unrotated_next_grid


def move_west(grid):
    grid = [r[::-1] for r in grid]
    next_grid = move_east(grid)
    return [r[::-1] for r in next_grid]


grid = []
with open("input.txt") as file:
    for line in file.readlines():
        grid.append(line.strip())

seen_soms = []
p = 0

for j in range(1, 500):
    grid = move_north(grid)
    grid = move_west(grid)
    grid = move_south(grid)
    grid = move_east(grid)

    som = 0
    for i, line in enumerate(grid[::-1]):
        som += (i + 1) * len([c for c in line if c == "O"])
    print(j, " som ", som)
    # if som == 104883:
    #     print(j)
    #     print(j - p)
    #     p = j
    seen_soms.append(som)
