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
        unfolded_line = line
        for _ in range(4):
            unfolded_line = unfolded_line + "?" + line
        line = unfolded_line
        groups = [int(c) for c in raw_groups.split(",")]
        groups = groups * 5
        question_index = [index for index, c in enumerate(line) if c == "?"]
        sharp_count = sum([1 for index, c in enumerate(line) if c == "#"])
        sharp_expected_count = sum(groups)
        print(line_number, line)

        for combination in itertools.combinations(question_index, sharp_expected_count - sharp_count):
            replaced_line = line
            for index in combination:
                replaced_line = replaced_line[:index] + "#" + replaced_line[index + 1:]

            counted_groups = count_groups(replaced_line)
            if counted_groups == groups:
                arrangements += 1
        print(arrangements)
