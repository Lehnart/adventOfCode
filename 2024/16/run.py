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

import enum
class Direction(enum.Enum):
    UP = 0
    RIGHT = 1 
    DOWN = 2
    LEFT = 3

xS, yS = find_positions(maze, "S")[0] 
xE, yE = find_positions(maze, "E")[0]
print(".:", len(find_positions(maze, ".")))

next_positions = [(xS,yS, Direction.RIGHT, 0)]
visited_positions = set()
score_min_per_position = {(xS,yS, Direction.RIGHT ) : 0}

step = 0
is_end =  False
while next_positions:
    step += 1 
    print("step", step)
    nn_positions = set()
    for x,y,ori,score in next_positions:
        visited_positions.add((x,y, ori))
        if ori == Direction.RIGHT : 
            c = get_at_position(maze, x+1, y)
            if c is None or c == "c" :
                continue 
            elif c in ".E" :
                if (x+1,y,ori) not in visited_positions:
                    nn_positions.add((x+1,y,ori, score + 1))
                    score_min_per_position[(x+1,y,ori)] = score + 1
                elif score_min_per_position[(x+1,y,ori)] >= score + 1 :
                    nn_positions.add((x+1,y,ori, score + 1))
                    score_min_per_position[(x+1,y,ori)] = score + 1

        elif ori == Direction.LEFT : 
            c = get_at_position(maze, x-1, y)
            if c is None or c == "c" :
                continue 
            elif c in ".E" :
                if (x-1,y,ori) not in visited_positions:
                    nn_positions.add((x-1,y,ori, score + 1))
                    score_min_per_position[(x-1,y,ori)] = score + 1
                elif score_min_per_position[(x-1,y,ori)] >= score + 1 :
                    nn_positions.add((x-1,y,ori, score + 1))
                    score_min_per_position[(x-1,y,ori)] = score + 1

        elif ori == Direction.DOWN : 
            c = get_at_position(maze, x, y+1)
            if c is None or c == "c" :
                continue 
            elif c in ".E" :
                if (x,y+1,ori) not in visited_positions:
                    nn_positions.add((x,y+1,ori, score + 1))
                    score_min_per_position[(x,y+1,ori)] = score + 1
                elif score_min_per_position[(x,y+1,ori)] >= score + 1 :
                    nn_positions.add((x,y+1,ori, score + 1))
                    score_min_per_position[(x,y+1,ori)] = score + 1

        elif ori == Direction.UP : 
            c = get_at_position(maze, x, y-1)
            if c is None or c == "c" :
                continue 
            elif c in ".E" :
                if (x,y-1,ori) not in visited_positions:
                    nn_positions.add((x,y-1,ori, score + 1))
                    score_min_per_position[(x,y-1,ori)] = score + 1
                elif score_min_per_position[(x,y-1,ori)] >= score + 1 :
                    nn_positions.add((x,y-1,ori, score + 1))
                    score_min_per_position[(x,y-1,ori)] = score + 1

        if (x,y,Direction((ori.value+1)%4)) not in visited_positions:
            nn_positions.add((x,y,Direction((ori.value+1)%4), score+1000))
            score_min_per_position[(x,y,Direction((ori.value+1)%4))] = score + 1000

        elif score_min_per_position[(x,y,Direction((ori.value+1)%4))] >= score+1000 :
            nn_positions.add((x,y,Direction((ori.value+1)%4), score+1000))
            score_min_per_position[(x,y,Direction((ori.value+1)%4))] = score + 1000

        if (x,y,Direction((ori.value+3)%4)) not in visited_positions:
            nn_positions.add((x,y,Direction((ori.value+3)%4), score+1000))
            score_min_per_position[(x,y,Direction((ori.value+3)%4))] = score + 1000

        elif score_min_per_position[(x,y,Direction((ori.value+3)%4))] >= score+1000 :
            nn_positions.add((x,y,Direction((ori.value+3)%4), score+1000))
            score_min_per_position[(x,y,Direction((ori.value+3)%4))] = score + 1000

    next_positions = nn_positions

print(step)
print(score_min_per_position[(xE,yE,Direction.DOWN)])
print(score_min_per_position[(xE,yE,Direction.UP)])
print(score_min_per_position[(xE,yE,Direction.LEFT)])
print(score_min_per_position[(xE,yE,Direction.RIGHT)])