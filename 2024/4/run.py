import os 
raw_grid = []

with open("input.txt","r") as f:
    for line in f.readlines():
        raw_grid.append(list(line.strip()))

class Grid:
    def __init__(self, grid) -> None:
        self.grid = grid

    def get(self, x, y):
        if 0 > y or y >= len(self.grid):
            return ' ' 
        if 0 > x or x >= len(self.grid[y]):
            return ' ' 
        return self.grid[y][x]

    def size(self):
        return (len(self.grid[0]), len(self.grid) )
    


count = 0
xcount = 0
grid = Grid(raw_grid)
for y in range(grid.size()[1]):
    for x in range(grid.size()[0]) :
        
        h_word = grid.get(x,y) + grid.get(x+1,y) +grid.get(x+2,y) +grid.get(x+3,y) 
        rh_word = grid.get(x,y) + grid.get(x-1,y) +grid.get(x-2,y) +grid.get(x-3,y) 
        v_word = grid.get(x,y) + grid.get(x,y+1) +grid.get(x,y+2) +grid.get(x,y+3) 
        rv_word = grid.get(x,y) + grid.get(x,y-1) +grid.get(x,y-2) +grid.get(x,y-3) 
        rd_word = grid.get(x,y) + grid.get(x+1,y+1) +grid.get(x+2,y+2) +grid.get(x+3,y+3)
        ru_word = grid.get(x,y) + grid.get(x+1,y-1) +grid.get(x+2,y-2) +grid.get(x+3,y-3)
        ld_word = grid.get(x,y) + grid.get(x-1,y+1) +grid.get(x-2,y+2) +grid.get(x-3,y+3)
        lu_word = grid.get(x,y) + grid.get(x-1,y-1) +grid.get(x-2,y-2) +grid.get(x-3,y-3)
        
        if h_word == "XMAS":
            count += 1
        if rh_word == "SAMX":
            count += 1
        if v_word == "XMAS":
            count += 1
        if rv_word == "SAMX":
            count += 1
        if rd_word == "XMAS":
            count += 1
        if ru_word == "XMAS":
            count += 1
        if ld_word == "XMAS":
            count += 1
        if lu_word == "XMAS":
            count += 1

        xtl_word = grid.get(x-1,y-1) + grid.get(x,y) + grid.get(x+1,y+1)
        xbl_word = grid.get(x-1,y+1) + grid.get(x,y) + grid.get(x+1,y-1)

        if xtl_word in ["MAS", "SAM"] and xbl_word in ["MAS", "SAM"]:
            xcount +=1 
        
print(count)
print(xcount)