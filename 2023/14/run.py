next_grid = []
with open("input.txt") as file:
    for row_index, line in enumerate(file):
        next_grid.append("")
        for c_index, c in enumerate(line.strip()):
            if c in ".#":
                next_grid[-1] += c
            elif c == "O":
                j = row_index - 1
                while j >= 0 and next_grid[j][c_index] == ".":
                    j -= 1
                next_grid[j + 1] = next_grid[j + 1][:c_index] + "O" + next_grid[j + 1][c_index + 1:]
                if j != row_index - 1:
                    next_grid[row_index]= next_grid[row_index][:c_index] + "." + next_grid[row_index][c_index + 1:]
            else :
                raise Exception
som = 0
for i,line in enumerate(next_grid[::-1]):
    som += (i+1)*len([c for c in line if c == "O"])
print(som)