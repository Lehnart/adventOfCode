class Level():

    def __init__(self, levels) -> None:
        self.levels = levels

    def is_increasing(self):
        if self.levels[0] < self.levels[1]:
            return True 
        if self.levels[0] > self.levels[1]:
            return False
        return None

    def is_safe(self):
        increasing : bool = self.is_increasing()
        if increasing is None :
            return False 
        for index in range(len(self.levels)-1):
            if increasing and (self.levels[index] >= self.levels[index+1]):
                return False
        
            if not increasing and (self.levels[index] <= self.levels[index+1]):
                return False

            if not(1 <= abs(self.levels[index] - self.levels[index+1]) <= 3):
                return False 
        return True 

    def is_safe_with_dampening(self):
        if self.is_safe() : 
            return True
        for index in range(len(self.levels)):
            dampened_level_row = list(self.levels)
            dampened_level_row.pop(index)
            dampened_level = Level(dampened_level_row)
            if dampened_level.is_safe() :
                return True 
        return False 
    
level_array = []
with open("input.txt","r") as f:
    for line in f.readlines():
        level_row = [ int(c) for c in line.split()]
        level_array.append(level_row) 

safe_count = 0
for level_row in level_array:
    if Level(level_row).is_safe():
        safe_count += 1 
print(safe_count)

dampened_safe_count = 0
for level_row in level_array:
    if Level(level_row).is_safe_with_dampening():
        dampened_safe_count += 1 
print(dampened_safe_count)