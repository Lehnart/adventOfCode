from typing import List, Callable


class Monkey:

    def __init__(self, id: int, items: List[int], operation: Callable[[int], int], test: Callable[[int], int]):
        self.id = id
        self.items = items
        self.operation = operation
        self.test = test
        self.inspections = 0

    def add_item(self, item : int):
        self.items.append(item)

    def process(self, monkeys):
        #print("Monkey "+ str(self.id) + ":")
        for i in range(len(self.items)):
            item = self.items[i]
            #print(f"Monkey inspects an item ith a worry level of {item}")
            item = self.operation(item)
            #print(f"Worry level is after inspection {item}")
            #item = item // 3
            #print(f"Worry level is after bored {item}")
            monkeys[self.test(item)].add_item(item)
            #print(f"Item is thrown to {self.test(item)}")
            self.inspections += 1
        self.items.clear()

monkey0 = Monkey(0, [71, 56, 50, 73], lambda x: x * 11, lambda x: 1 if x % 13 == 0 else 7)
monkey1 = Monkey(1, [70, 89, 82], lambda x: x + 1, lambda x: 3 if x % 7 == 0 else 6)
monkey2 = Monkey(2, [52, 95], lambda x: x * x, lambda x: 5 if x % 3 == 0 else 4)
monkey3 = Monkey(3, [94, 64, 69, 87, 70], lambda x: x + 2, lambda x: 2 if x % 19 == 0 else 6)
monkey4 = Monkey(4, [98, 72, 98, 53, 97, 51], lambda x: x + 6, lambda x: 0 if x % 5 == 0 else 5)
monkey5 = Monkey(5, [79], lambda x: x + 7, lambda x: 7 if x % 2 == 0 else 0)
monkey6 = Monkey(6, [77, 55, 63, 93, 66, 90, 88, 71], lambda x: x * 7, lambda x: 2 if x % 11 == 0 else 4)
monkey7 = Monkey(7, [54, 97, 87, 70, 59, 82, 59], lambda x: x + 8, lambda x: 1 if x % 17 == 0 else 3)
monkeys = [monkey0, monkey1, monkey2, monkey3, monkey4, monkey5, monkey6, monkey7]

for it in range(10000):
    print(it)
    for monkey in monkeys:
        monkey.process(monkeys)

for monkey in monkeys :
    print(monkey.inspections)
