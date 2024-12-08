antenna_map = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        antenna_map.append([])
        for c in line.strip():
            antenna_map[-1].append(c)

antenna_positions = {}
for y in range(len(antenna_map)):
    for x in range(len(antenna_map[y])):
        c = antenna_map[y][x]
        if c == '.':
            continue 
        if c not in antenna_positions :
            antenna_positions[c] = []
        antenna_positions[c].append((x,y))

def is_correct_antinode_position(p1, p2, width, height, pos):
    if pos[0] < 0 or pos[0] >= width :
        return False 
    if pos[1] < 0 or pos[1] >= height :
        return False 
    return True 

width = len(antenna_map[0])
height = len(antenna_map)
print(width, height)
antinode_positions = set()
for frequency in antenna_positions.keys():
    positions = antenna_positions[frequency]
    for i in range(len(positions)):
        for j in range(i+1, len(positions)):
            p1 = positions[i]
            p2 = positions[j]
            print(p1, p2)

            dx0 = p1[0] - p2[0]
            dy0 = p1[1] - p2[1]

            dx = dx0 
            dy = dy0
            while abs(dx) < width and abs(dy) < height:

                if is_correct_antinode_position(p1, p2, len(antenna_map[0]), len(antenna_map), (p1[0]+dx, p1[1] + dy) ):
                    antinode_positions.add( (p1[0]+dx, p1[1] + dy) )
                if is_correct_antinode_position(p1, p2, len(antenna_map[0]), len(antenna_map),  (p2[0]-dx, p2[1] - dy) ):
                    antinode_positions.add(  (p2[0]-dx, p2[1] - dy) )
                if is_correct_antinode_position(p1, p2, len(antenna_map[0]), len(antenna_map),  (p1[0]-dx, p1[1] - dy)):
                    antinode_positions.add(  (p1[0]-dx, p1[1] - dy) )
                if is_correct_antinode_position(p1, p2, len(antenna_map[0]), len(antenna_map),(p2[0]+dx, p2[1] + dy)):
                    antinode_positions.add((p2[0]+dx, p2[1] + dy) )

                print(dx,dy)
                print( (p1[0]-dx, p1[1] - dy) )
                print((p2[0]+dx, p2[1] + dy) )
                dx += dx0  
                dy += dy0
print(antinode_positions)
print(len(antinode_positions))