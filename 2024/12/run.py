import enum
class FenceType(enum.Enum):
    LEFT=1
    RIGHT=2
    TOP=3
    BOTTOM=4

def read_garden():
    garden = []
    with open("input.txt","r") as f :
        for line in f.readlines():
            garden.append([])
            for c in line.strip():
                garden[-1].append(c)
    return garden

def find_unvisited_positions(garden, visited_positions):
    for y in range(len(garden)):
        for x in range(len(garden)):
            if not visited_positions[y][x]:
                return (x,y)
    return None

def get_plant(garden, x, y):
    if y < 0 or y >= len(garden):
        return None 
    if x < 0 or x >= len(garden[y]):
        return None 
    return garden[y][x]

def find_region(start, garden, visited_positions):
    x0,y0 = start
    plant = get_plant(garden, x0,y0)
    region = set([start])

    next_positions = [start]
    while next_positions:
        nnext_positions = set()
        for position in next_positions :
            x,y = position
            if visited_positions[y][x] :
                continue 

            p = get_plant(garden, x+1, y)
            if p == plant and not visited_positions[y][x+1] :
                nnext_positions.add((x+1,y))
                region.add((x+1,y))

            p = get_plant(garden, x-1, y)
            if p == plant and not visited_positions[y][x-1]:
                nnext_positions.add((x-1,y))
                region.add((x-1,y))

            p = get_plant(garden, x, y+1)
            if p == plant and not visited_positions[y+1][x]:
                nnext_positions.add((x,y+1))
                region.add((x,y+1))

            p = get_plant(garden, x, y-1)
            if p == plant and not visited_positions[y-1][x]:
                nnext_positions.add((x, y-1))
                region.add((x,y-1))
                
            visited_positions[y][x] = True 
        next_positions = nnext_positions
    return region


garden = read_garden()
regions = {}
visited_positions = [[False for _ in range(len(garden[0]))] for _ in range(len(garden))]

unvisited_position = find_unvisited_positions(garden, visited_positions)
while unvisited_position is not None:
    x,y = unvisited_position
    plant = garden[y][x]
    if plant not in regions:
        regions[plant] = []
    regions[plant].append(find_region( (x,y), garden , visited_positions))
    unvisited_position = find_unvisited_positions(garden, visited_positions)

count = 0
for plant in regions:
    for region in regions[plant]:
        fences = set()
        for position in region:
            x,y = position 

            p = get_plant(garden, x-1, y)
            if p != plant :
                fences.add((x-1,y, FenceType.RIGHT))

            p = get_plant(garden, x+1, y)
            if p != plant :
                fences.add((x+1,y, FenceType.LEFT))

            p = get_plant(garden, x, y-1)
            if p != plant :
                fences.add((x,y-1, FenceType.BOTTOM))

            p = get_plant(garden, x, y+1)
            if p != plant :
                fences.add((x,y+1, FenceType.TOP))

        count += len(fences)*len(region)

print(count)