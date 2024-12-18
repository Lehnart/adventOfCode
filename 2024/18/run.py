def get_at_position(grid,x,y):
    if y < 0 or y >= len(grid) :
        return None 
    if x < 0 or x >= len(grid[y]):
        return None 
    return grid[y][x] 

corrupted_bytes = []
with open("input.txt","r") as f:
    for line in f.readlines():
        raw_x,raw_y = line.strip().split(",")
        x,y = int(raw_x), int(raw_y)
        corrupted_bytes.append((x,y))

print(corrupted_bytes)


for i in range(1024, len(corrupted_bytes)):

    maze = [['.' for _ in range(0,71)] for _ in range(0,71)]
    for b in corrupted_bytes[:i] :
        x,y = b 
        maze[y][x] = "#"

    xS, yS = (0,0)
    xE, yE = (70,70)

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
            if c == "." :
                if (x+1,y) not in visited_positions:
                    nn_positions.add((x+1,y))

            c = get_at_position(maze, x-1, y)
            if c == "." :
                if (x-1,y) not in visited_positions:
                    nn_positions.add((x-1,y))
            
            c = get_at_position(maze, x, y+1)
            if c == "." :
                if (x,y+1) not in visited_positions:
                    nn_positions.add((x,y+1))

            c = get_at_position(maze, x, y-1)
            if c == "." :
                if (x,y-1) not in visited_positions:
                    nn_positions.add((x,y-1))
        next_positions = nn_positions
    print(i, step, is_end, corrupted_bytes[:i][-1])