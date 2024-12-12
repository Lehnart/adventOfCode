class Stone:

    def __init__(self, number, next_stone = None):
        self.number = number 
        self.next_stone = next_stone

    def blink(self):
        if self.number == 0 :
            self.number=1 
            return self.next_stone
        elif len(str(self.number)) % 2 == 0:
            number_str = str(self.number)
            left, right = int(number_str[:len(number_str)//2]), int(number_str[len(number_str)//2:]) 
            new_stone = Stone(right, self.next_stone)
            self.number = left 
            self.next_stone = new_stone
            return new_stone.next_stone
        else :
            self.number *= 2024 
            return self.next_stone

class Cache:

    def __init__(self):
        self.cache = {}

    def get(self, number, generation):
        if number not in self.cache:
            self.cache[number] = {}
        if generation not in self.cache[number]:
            self.cache[number][generation] = self.compute(number, generation)
        return self.cache[number][generation]

    def compute(self, number, generation):
        if number not in self.cache:
            self.cache[number] = {}
        if generation not in self.cache[number]:
            self.cache[number][generation] = {}

        if generation == 1:
            if number == 0 :
                self.cache[number][generation] = {1:1}

            elif len(str(number)) % 2 == 0:
                number_str = str(number)
                left, right = int(number_str[:len(number_str)//2]), int(number_str[len(number_str)//2:]) 
                if left == right :
                    self.cache[number][generation] = {left:2}
                else:
                    self.cache[number][generation] = {left:1, right:1}
            else :
                self.cache[number][generation] = {number * 2024 :1}
        else :
            previous_generation = self.get(number, generation-1)         
            current_generation = {}   
            for stone_number in previous_generation.keys():
                stone_count = previous_generation[stone_number]
                stone_next_gen = self.compute(stone_number, 1)
                for k in stone_next_gen.keys():
                    if k not in current_generation:
                        current_generation[k] = 0
                    current_generation[k] += stone_count*stone_next_gen[k] 
                
            self.cache[number][generation] = current_generation

        return self.cache[number][generation]            


numbers = []
with open("input.txt","r") as f:
    numbers = [ int(n) for n in f.read().split() ]

stone_0 = None
current_stone = None
for n in numbers:
    if current_stone is None :
        stone_0 = Stone(n)
        current_stone = stone_0
    else :
        current_stone.next_stone = Stone(n)
        current_stone = current_stone.next_stone


def get_blink_stones(stone_0, n_runs) :
    for i in range(n_runs):
        current_stone = stone_0
        while current_stone is not None :
            current_stone = current_stone.blink()

        current_stone = stone_0
        numbers = []
        while current_stone is not None :
            numbers.append(current_stone.number)
            current_stone = current_stone.next_stone
    return numbers

cache = Cache()
count = 0
for n in numbers:
    r = cache.get(n, 75)
    for k in r :
        count += r[k]
print(count)
