class ElfCaloryCounter:

    def __init__(self):
        self.current_calories = 0
        self.calories_array = []

    def nextElf(self):
        self.calories_array.append(self.current_calories)
        self.current_calories = 0


calory_counter = ElfCaloryCounter()
with open("input.txt") as input_file:
    for line in input_file:
        if line.strip() == "":
            calory_counter.nextElf()
        else:
            calory_counter.current_calories += int(line)

calory_counter.calories_array.sort(reverse=True)
print(calory_counter.calories_array)
print(max(calory_counter.calories_array))
print(sum(calory_counter.calories_array[:3]))
