class Ranger:

    def __init__(self):
        self.count = 0
        self.count2 = 0

    def process(self, lo1: int, hi1: int, lo2: int, hi2: int):
        if lo1 >= lo2 and hi1 <= hi2:
            self.count += 1

        elif lo2 >= lo1 and hi2 <= hi1:
            self.count += 1

    def process2(self, lo1: int, hi1: int, lo2: int, hi2: int):
        if hi2 >= lo1 >= lo2:
            self.count2 += 1

        elif hi1 >= lo2 >= lo1:
            self.count2 += 1

        elif hi2 >= hi1 >= lo2:
            self.count2 += 1

        elif hi1 >= hi2 >= lo1:
            self.count2 += 1


ranger = Ranger()
with open("input.txt") as file:
    for line in file:
        range1, range2 = line.strip().split(",")
        lo1, hi1 = [int(r) for r in range1.split("-")]
        lo2, hi2 = [int(r) for r in range2.split("-")]
        ranger.process(lo1, hi1, lo2, hi2)
        ranger.process2(lo1, hi1, lo2, hi2)
    print(ranger.count)
    print(ranger.count2)

