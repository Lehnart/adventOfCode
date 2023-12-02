class Rucksack:

    def __init__(self):
        self.priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.score = 0
        self.score2 = 0

    def process(self, items : str):
        i = len(items)//2
        compartment1 = items[:i]
        compartment2 = items[i:]

        shared_items = set([c for c in compartment1 if c in compartment2])
        for shared_item in shared_items:
            self.score += self.priorities.index(shared_item)+1

    def process2(self, items1 : str, items2 : str, items3 : str):
        shared_items = set([c for c in items1 if c in items2 and c in items3])
        for shared_item in shared_items:
            self.score2 += self.priorities.index(shared_item)+1

rucksack = Rucksack()
with open("input.txt") as file:
    line_number = 0
    lines = []
    for line in file:
        rucksack.process(line.strip())
        lines.append(line.strip())
        if (line_number+1) % 3 == 0:
            rucksack.process2(*lines)
            lines.clear()
        line_number += 1

print(rucksack.score)
print(rucksack.score2)
