from typing import List


class Position:

    def __init__(self, x, y, alt):
        self.x = x
        self.y = y
        self.alt = alt

    def tuple(self):
        return self.x, self.y, self.alt


class Path:

    def __init__(self, positions: List[Position]):
        self.positions = positions

    def starting_position(self):
        return self.positions[0]

    def ending_position(self):
        return self.positions[-1]

    def is_position_in_path(self, x, y):
        for position in self.positions:
            if position.x == x and position.y == y:
                return True
        return False

    def is_possible_step(self, alt_start, alt_end):
        return alt_start <= alt_end + 1

    def check_position(self, alt, next_x, next_y, alt_grid, next_paths):
        if next_x < 0 or next_x >= len(alt_grid[0]):
            return

        if next_y < 0 or next_y >= len(alt_grid):
            return

        if self.is_position_in_path(next_x, next_y):
            return

        next_alt = alt_grid[next_y][next_x]
        if self.is_possible_step(alt, next_alt):
            next_positions = list(self.positions)
            next_positions.append(Position(next_x, next_y, next_alt))
            next_paths.append(Path(next_positions))

    def expand_path(self, grid):
        next_paths = []
        x, y, alt = self.ending_position().tuple()
        self.check_position(alt, x+1, y, grid, next_paths)
        self.check_position(alt, x-1, y, grid, next_paths)
        self.check_position(alt, x, y+1, grid, next_paths)
        self.check_position(alt, x, y-1, grid, next_paths)

        return next_paths


grid = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        grid.append([])
        for c in line.strip():
            grid[-1].append(c)


def get_character_position(grid, character):
    positions = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == character:
                positions.append((x, y))
    return positions

def convert_grid_to_int(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            grid[y][x] = ord(grid[y][x])


starting_position = get_character_position(grid, 'S')[0]
ending_position = get_character_position(grid, 'E')[0]

grid[starting_position[1]][starting_position[0]] = 'a'
grid[ending_position[1]][ending_position[0]] = 'z'

convert_grid_to_int(grid)

counter = 0
print(counter)
counter += 1
visited_positions = set((ending_position[0], ending_position[1]))

paths = [Path([Position(ending_position[0], ending_position[1], ord('z'))])]
while paths != []:
    next_paths = []
    for path in paths:
        expanded_paths = path.expand_path(grid)
        next_paths.extend(expanded_paths)
    paths = next_paths
    
    to_remove = []
    for i in range(len(next_paths)):
        path = next_paths[i]
        x,y,_ = path.ending_position().tuple()
        if(x,y) in visited_positions:
            to_remove.append(i)
        else : 
            visited_positions.add((x,y))
    for i in to_remove[::-1]:
        next_paths.pop(i)
    
    for path in next_paths :        
        end_x, end_y, end_alt = path.ending_position().tuple()
        start_x, start_y, _ = path.starting_position().tuple()
        if end_alt == ord('a') and ending_position == (start_x, start_y):
            print(len(path.positions)-1) 
            