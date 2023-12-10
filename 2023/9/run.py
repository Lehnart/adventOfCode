histories = []
the_sum = 0
backward_sum = 0

with open("input.txt") as file:
    for line in file:
        histories.append([int(c) for c in line.strip().split(" ")])
for history in histories:
    diffs = []
    diffs.append(history)
    while not all(c == 0 for c in diffs[-1]):
        diffs.append([diffs[-1][i + 1] - diffs[-1][i] for i in range(len(diffs[-1]) - 1)])

    diffs[-1].append(0)
    diffs[-1].insert(0, 0)
    for i, diff in enumerate(diffs[::-1]):
        if i == 0:
            continue
        diff.append(diff[-1] + diffs[::-1][i - 1][-1])
        diff.insert(0, diff[0] - diffs[::-1][i - 1][0])
    for diff in diffs:
        print(diff)
    print(diffs[0][-1])
    the_sum += diffs[0][-1]
    backward_sum += diffs[0][0]

print(the_sum)
print(backward_sum)