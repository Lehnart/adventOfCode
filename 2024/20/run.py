maze = []
with open("input.txt","r") as f:
    for line in f.readlines():
        maze.append([])
        for c in line.strip():
            maze[-1].append(c)

def find_positions(grid, c):
    positions = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if c == grid[y][x] :
                positions.append((x,y))
    return positions

def get_at_position(grid,x,y):
    if y < 0 or y >= len(grid) :
        return None 
    if x < 0 or x >= len(grid[y]):
        return None 
    return grid[y][x] 



xS, yS = find_positions(maze, "S")[0]
xE, yE = find_positions(maze, "E")[0]
walls = find_positions(maze, "#")
count = 0 
print(len(walls))
for index, wall in enumerate(walls) :
    print(index)
    xw, yw = wall 
    maze[yw][xw] = "."

    next_positions = [(xS,yS)]
    visited_positions = set()
    step = 0
    is_end =  False
    while next_positions and not is_end:

        step += 1 
        nn_positions = set()
        for x,y in next_positions:
            if (x,y) == (xE, yE) :
                is_end = True 
                break 
            visited_positions.add((x,y))

            c = get_at_position(maze, x+1, y)            
            if c is not None and c in "SE." :
                if (x+1,y) not in visited_positions:
                    nn_positions.add((x+1,y))

            c = get_at_position(maze, x-1, y)
            if  c is not None and c in "SE." :
                if (x-1,y) not in visited_positions:
                    nn_positions.add((x-1,y))
            
            c = get_at_position(maze, x, y+1)
            if c is not None and c in "SE." :
                if (x,y+1) not in visited_positions:
                    nn_positions.add((x,y+1))

            c = get_at_position(maze, x, y-1)
            if  c is not None and c in "SE." :
                if (x,y-1) not in visited_positions:
                    nn_positions.add((x,y-1))
        next_positions = nn_positions
    if step <= 9237 and is_end :
        count += 1
    maze[yw][xw] = "#"

print(count)
