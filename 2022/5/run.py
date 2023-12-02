import copy


class CrateArrangement:

    def __init__(self, crate_array):
        self.crate_array = crate_array

    def print(self):
        for row in self.crate_array:
            print(row)

    def move(self, move):
        move_count, crate_from, crate_to = move
        for i in range(move_count):
            self.move_crate(crate_from, crate_to)

    def move_crate(self, crate_from, crate_to):
        moved_crate = self.take_crate(crate_from)
        self.drop_crate(moved_crate, crate_to)

    def take_crate(self, crate_from):
        row_index = 0
        moved_crate = ' '
        while row_index < len(self.crate_array):
            if self.crate_array[row_index][crate_from - 1] == ' ':
                row_index += 1
                continue
            else:
                moved_crate = self.crate_array[row_index][crate_from - 1]
                self.crate_array[row_index][crate_from - 1] = ' '
                break
        return moved_crate

    def drop_crate(self, moved_crate, crate_to):
        row_index = len(self.crate_array) - 1
        while row_index >= 0:
            if self.crate_array[row_index][crate_to - 1] != ' ':
                row_index -= 1
                continue
            else:
                self.crate_array[row_index][crate_to - 1] = moved_crate
                break

    def find_top_crates(self):
        crates = ""
        for col in range(0, 9):
            for row in range(0, len(self.crate_array)):
                if self.crate_array[row][col] != ' ':
                    crates += self.crate_array[row][col]
                    break
        return crates


class CrateArrangement9001:

    def __init__(self, crate_array):
        self.crate_array = crate_array

    def print(self):
        for row in self.crate_array:
            print(row)

    def move(self, move):
        move_count, crate_from, crate_to = move
        self.move_crates(move_count, crate_from, crate_to)

    def move_crates(self, crate_count, crate_from, crate_to):
        moved_crates = self.take_crates(crate_count, crate_from)
        self.drop_crates(moved_crates, crate_to)

    def take_crates(self, crate_count, crate_from):
        row_index = 0
        moved_crates = []
        while row_index < len(self.crate_array) and len(moved_crates) < crate_count:
            if self.crate_array[row_index][crate_from - 1] != ' ':
                moved_crates.append(self.crate_array[row_index][crate_from - 1])
                self.crate_array[row_index][crate_from - 1] = ' '
            row_index += 1
        return moved_crates

    def drop_crates(self, moved_crates, crate_to):
        row_index = len(self.crate_array) - 1
        while row_index >= 0 and len(moved_crates) > 0:
            if self.crate_array[row_index][crate_to - 1] == ' ':
                self.crate_array[row_index][crate_to - 1] = moved_crates.pop()
            row_index -= 1

    def find_top_crates(self):
        crates = ""
        for col in range(0, 9):
            for row in range(0, len(self.crate_array)):
                if self.crate_array[row][col] != ' ':
                    crates += self.crate_array[row][col]
                    break
        return crates


with open("input.txt") as file:
    file_content = file.readlines()

    crate_arrangement = file_content[:8]
    crate_row_list = [[' '] * 9 for i in range(60)]
    for line in crate_arrangement:
        crate_line = line[1::4]
        crate_row_list.append([*crate_line])

    crates = CrateArrangement(copy.deepcopy(crate_row_list))
    crates2 = CrateArrangement9001(copy.deepcopy(crate_row_list))

    moves_raw = file_content[10:]
    moves = []
    for move in moves_raw:
        splitted_move = move.replace("move", "").replace("from", "").replace("to", "").strip().split()
        move_int = [int(c) for c in splitted_move]
        moves.append(move_int)

    for move in moves[::]:
        crates.move(move)
        crates2.move(move)

    print(crates.find_top_crates())
    print(crates2.find_top_crates())
