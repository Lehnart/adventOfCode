import itertools


def count_groups(line):
    groups = []
    is_in_group = False
    for c in line:
        if c == "#":
            if not is_in_group:
                groups.append(0)
                is_in_group = True
            groups[-1] += 1
        else:
            is_in_group = False
    return groups

arrangements = 0
with open("input.txt") as file:
    for line_number, line in enumerate(file):
        line, raw_groups = line.strip().split(" ")
        groups = [int(c) for c in raw_groups.split(",")]
        question_index = [index for index, c in enumerate(line) if c == "?"]
        print(line_number, line)
        for product in itertools.product(".#", repeat=len(question_index)):
            replaced_line = line
            for index, c in enumerate(product):
                c_index = question_index[index]
                replaced_line = replaced_line[:c_index] + c + replaced_line[c_index + 1:]

            counted_groups = count_groups(replaced_line)
            if counted_groups == groups:
                arrangements += 1
        print(arrangements)
