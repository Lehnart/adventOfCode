class HeightGrid :

    def __init__(self, grid) -> None:
        self.grid = grid

    def get_starting_positions(self):
        positions = []
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x] == 0 :
                    positions.append((x,y))
        return positions

    def get_height(self, x, y):
        if x < 0 or x >= len(self.grid[0]) or y < 0 or y >= len(self.grid):
            return None
        return self.grid[y][x]

    def find_trail_ends(self, starting_position):
        current_positions = [starting_position]
        current_height = 0
        while current_positions != [] and current_height < 9 :
            next_positions = []
            for current_position in current_positions:
                next_positions_from_current = self.find_next_positions(current_position, current_height)
                if next_positions_from_current :
                    next_positions.extend(next_positions_from_current)
            current_positions = next_positions
            current_height += 1
            
        return current_positions

    def find_next_positions(self, position, height):
        x, y = position
        next_positions = []
        if (next_height := self.get_height(x+1, y)) is not None :
            if next_height == height + 1: next_positions.append((x+1,y))
        if (next_height := self.get_height(x-1, y)) is not None :
            if next_height == height + 1: next_positions.append((x-1,y))
        if (next_height := self.get_height(x, y+1)) is not None :
            if next_height == height + 1: next_positions.append((x,y+1))
        if (next_height := self.get_height(x, y-1)) is not None : 
            if next_height == height + 1: next_positions.append((x,y-1))
        return next_positions
    
def get_height_grid():
    height_grid = []
    with open("input.txt","r") as f:
        for line in f.readlines():
            height_grid.append([])
            for c in line.strip():
                height_grid[-1].append(int(c))
    return height_grid


height_grid = HeightGrid(get_height_grid())
starting_positions = height_grid.get_starting_positions()
trail_head_count = 0 
trail_rating_count = 0
for starting_position in starting_positions:
    ends = height_grid.find_trail_ends(starting_position)
    trail_rating_count += len(ends)
    trail_heads = set(ends)
    trail_head_count += len(trail_heads)
print(trail_head_count)
print(trail_rating_count)