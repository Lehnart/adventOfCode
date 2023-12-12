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


def count_arrangement(current_line, line, expected_groups):
    while len(current_line) != len(line) and line[len(current_line)] != "?":
        current_line = current_line + line[len(current_line)]

    current_groups = count_groups(current_line)
    if len(current_groups) > len(expected_groups):
        return 0
    if len(current_groups) == len(expected_groups):
        return 1 if current_groups == expected_groups else 0

    for index in range(len(current_groups) - 1):
        if current_groups[index] != expected_groups[index]:
            return 0

    if len(current_groups)>0 and current_groups[-1] > expected_groups[-1]:
        return 0

    return count_arrangement(current_line + "#", line, expected_groups) + count_arrangement(current_line + ".", line, expected_groups)


arrangements = 0
with open("input.txt") as file:
    for line_number, line in enumerate(file):
        line, raw_groups = line.strip().split(" ")
        groups = [int(c) for c in raw_groups.split(",")]
        question_index = [index for index, c in enumerate(line) if c == "?"]
        sharp_count = sum([1 for index, c in enumerate(line) if c == "#"])
        sharp_expected_count = sum(groups)
        print(line_number, line)

        arrangements += count_arrangement("", line, groups)
        print(arrangements)
