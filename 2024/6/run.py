def get_map():
    map = []
    with open("input.txt", "r") as f:
        for line in f.readlines():
            map.append([])
            for c in line.strip():
                map[-1].append(c)
            
    return map 

guard_turn = {">": "v", "v": "<", "<": "^", "^": ">"}
map= get_map()
guard_position = None
guard_direction = ""
for y in range(len(map)):
    for x in range(len(map)):
        if map[y][x] in "<>v^":
            guard_position = (x, y)
            guard_direction = map[y][x]

starting_position = guard_position 
starting_direction = guard_direction

def walk(starting_position, starting_direction, map):
    guard_position = starting_position
    guard_direction = starting_direction
    guard_positions = set()
    guard_positions.add(guard_position)
    direction_per_position = {}
    is_in_loop = False
    while True:

        next_position = None
        if guard_direction == "^":
            next_position = (guard_position[0], guard_position[1] - 1)
        if guard_direction == "<":
            next_position = (guard_position[0]-1, guard_position[1])
        if guard_direction == ">":
            next_position = (guard_position[0]+1, guard_position[1])
        if guard_direction == "v":
            next_position = (guard_position[0], guard_position[1]+1)

        nx, ny = next_position
        if nx < 0 or nx >= len(map[0]) or ny < 0 or ny >= len(map) :
            break
        if map[ny][nx] == '#':
            guard_direction = guard_turn[guard_direction]
        else:
            guard_position = next_position

        guard_positions.add(guard_position)
        if next_position not in direction_per_position :
            direction_per_position[next_position] = [guard_direction]
        else :
            if guard_direction in direction_per_position[next_position]:
                is_in_loop = True 
                break
            else :
                direction_per_position[next_position].append(guard_direction)            
        
    return guard_positions, is_in_loop 

guard_positions, is_in_loop = walk(starting_position, starting_direction, map)    
print(len(guard_positions))

count = 0
for passing_position in list(guard_positions):
    x, y = passing_position
    map[y][x] = '#'
    _, is_in_loop = walk(starting_position, starting_direction, map)
    if is_in_loop:
        count += 1
    map[y][x] = "."
print(count)