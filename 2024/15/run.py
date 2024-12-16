grid = []
with open("grid.txt","r") as f :
    for line in f.readlines():
        grid.append([])
        for c in line.strip() :
            if c == "O":
                grid[-1].append("[")
                grid[-1].append("]")
            if c == "#":
                grid[-1].append("#")
                grid[-1].append("#")
            if c == ".":
                grid[-1].append(".")
                grid[-1].append(".")                
            if c == "@" :
                grid[-1].append(c)
                grid[-1].append(".")

moves = []
with open("input.txt","r") as f :
    for line in f.readlines() :
        for c in line.strip():
            moves.append(c)

def find_positions(grid, c):
    positions = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if c == grid[y][x] :
                positions.append((x,y))
    return positions

def can_move(grid, object_pos, direction):
    sx, sy = object_pos 
    if direction == "<":
        sx -= 1 
    if direction == ">":
        sx += 1 
    if direction == "v":
        sy += 1 
    if direction == "^":
        sy -= 1 
    
    if grid[sy][sx] == ".":
        return True

    if grid[sy][sx] == "#":
        return False 
    
    if grid[sy][sx] == "[":
        if direction == ">" : 
            return can_move(grid, (sx+1, sy), direction) 
        if direction in "v^" : 
            return can_move(grid, (sx, sy), direction) and can_move(grid, (sx+1, sy), direction)

    if grid[sy][sx] == "]":
        if direction == "<" : 
            return can_move(grid, (sx-1, sy), direction) 
        if direction in "v^" : 
            return can_move(grid, (sx, sy), direction) and can_move(grid, (sx-1, sy), direction)
    
    raise Exception("blabla") 

def move_sub(grid,submarine_pos, direction):
    sx, sy = submarine_pos 
    nx, ny = sx, sy
    c = grid[sy][sx]

    if direction == "<":
        nx -= 1 
    if direction == ">":
        nx += 1 
    if direction == "v":
        ny += 1 
    if direction == "^":
        ny -= 1 
    
    if grid[ny][nx] == ".":
        grid[ny][nx] = c
        grid[sy][sx] = "."
        return (nx,ny)
        

    if grid[ny][nx] == "#":
        raise Exception("blabla2") 
    
    if grid[ny][nx] == "[":
        if direction in "<>":
            move_sub(grid, (nx, ny), direction) 
            grid[ny][nx] = c
            grid[sy][sx] = "."
            return (nx,ny)
        if direction in "v^":
            move_sub(grid, (nx, ny), direction) 
            move_sub(grid, (nx+1, ny), direction) 
            grid[ny][nx] = c
            grid[sy][sx] = "."
            return (nx,ny)

    if grid[ny][nx] == "]":
        if direction in "<>":
            move_sub(grid, (nx, ny), direction) 
            grid[ny][nx] = c
            grid[sy][sx] = "."
            return (nx,ny)
        if direction in "v^":
            move_sub(grid, (nx, ny), direction) 
            move_sub(grid, (nx-1, ny), direction) 
            grid[ny][nx] = c
            grid[sy][sx] = "."
            return (nx,ny)

    raise Exception("blabla2") 


submarine_pos = find_positions(grid, "@")[0]
for move in moves :
    if can_move(grid,submarine_pos, move) :
        submarine_pos = move_sub(grid,submarine_pos, move)

count = 0
box_pos = find_positions(grid, "[")
for pos in  box_pos:
    x,y = pos
    count += (100*y)+x
print(count)