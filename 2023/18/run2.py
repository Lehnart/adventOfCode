import sys

int_to_dir = {0: "R", 1: "D", 2: "L", 3: "U"}
with open("input.txt") as file:
    with open("input2.txt", "w") as output_file:
        for line in file:
            _, _, raw_hex_instruction = line.split()
            hex_instruction = raw_hex_instruction.replace("(", "").replace(")", "").replace("#", "")
            dir_int = int(hex_instruction[-1])
            output_file.write(int_to_dir[dir_int])
            output_file.write(" ")
            output_file.write(str(int(hex_instruction[:-1], 16)))
            output_file.write(" " + raw_hex_instruction)
            output_file.write("\n")

min_x, max_x, min_y, max_y = sys.maxsize, -sys.maxsize, sys.maxsize, -sys.maxsize

with open("input.txt") as file:
    current_pos = (0, 0)
    direction_move = {"U": (0, -1), "R": (1, 0), "D": (0, +1), "L": (-1, 0)}
    for line in file:
        direction, raw_count, _ = line.split()
        count = int(raw_count)
        dx, dy = direction_move[direction]
        dx, dy = dx * count, dy * count
        current_pos = (current_pos[0] + dx, current_pos[1] + dy)
        x, y = current_pos
        if x > max_x: max_x = x
        if x < min_x: min_x = x
        if y > max_y: max_y = y
        if y < min_y: min_y = y

digs = [[[], []] for _ in range(max_x - min_x + 1)]
dig_count = 0
with open("input.txt") as file:
    current_pos = (0, 0)
    direction_move = {"U": (0, -1), "R": (1, 0), "D": (0, +1), "L": (-1, 0)}
    for line in file:
        direction, raw_count, _ = line.split()
        count = int(raw_count)
        dx, dy = direction_move[direction]
        dx, dy = dx * count, dy * count
        next_pos = (current_pos[0] + dx, current_pos[1] + dy)
        x0, y0 = current_pos
        x1, y1 = next_pos

        lx = min(x0, x1)
        rx = max(x0, x1)
        if lx != rx:
            for x in range(lx + 1, rx):
                digs[x - min_x][0].append(y0)
        else:
            digs[x1 - min_x][1].append(y0)
            digs[x1 - min_x][1].append(y1)
        current_pos = next_pos

dig_count = 0
dig_cases = set()
for dig_index, dig in enumerate(digs):
    dig[0].sort()
    dig[1].sort()
    p_i = 0
    d_i = 0
    while True:

        if d_i > len(dig[0]) - 1:
            if p_i < len(dig[1]) - 1:
                dig_count += dig[1][p_i + 1] - dig[1][p_i] + 1
                for i in range(dig[1][p_i], dig[1][p_i + 1] + 1):
                    dig_cases.add((dig_index, i))
                p_i += 2
            else:
                break

        elif d_i == len(dig[0]) - 1:
            if p_i > len(dig[1]) - 1:
                break
            elif p_i == len(dig[1]) - 1:
                raise Exception
            else:
                if dig[0][d_i] > dig[1][p_i + 1]:
                    dig_count += dig[1][p_i + 1] - dig[1][p_i] + 1
                    for i in range(dig[1][p_i], dig[1][p_i + 1] + 1):
                        dig_cases.add((dig_index, i))
                    dig[0].insert(0, dig[1][p_i + 1] + 1)
                    dig[0].sort()
                    p_i += 2
                elif dig[1][p_i + 1] > dig[0][d_i] > dig[1][p_i]:
                    raise Exception
                else:
                    dig_count += dig[1][p_i + 1] - dig[0][d_i] + 1
                    dig[0].insert(d_i + 1, dig[1][p_i + 1] + 1)
                    for i in range(dig[0][d_i], dig[1][p_i + 1] + 1):
                        dig_cases.add((dig_index, i))
                    d_i += 1
                    p_i += 2

        else:
            if p_i == len(dig[1]) - 1:
                raise Exception
            elif p_i > len(dig[1]) - 1:
                dig_count += dig[0][d_i + 1] - dig[0][d_i] + 1
                for i in range(dig[0][d_i], dig[0][d_i + 1] + 1):
                    dig_cases.add((dig_index, i))
                d_i += 2
            else:
                if dig[0][d_i] > dig[1][p_i + 1]:
                    dig_count += dig[1][p_i + 1] - dig[1][p_i] + 1
                    for i in range(dig[1][p_i], dig[1][p_i + 1] + 1):
                        dig_cases.add((dig_index, i))
                    dig[0].insert(0, dig[1][p_i + 1] + 1)
                    dig[0].sort()
                    p_i += 2

                elif dig[0][d_i + 1] < dig[1][p_i]:
                    dig_count += dig[0][d_i + 1] - dig[0][d_i] + 1
                    for i in range(dig[0][d_i], dig[0][d_i + 1] + 1):
                        dig_cases.add((dig_index, i))
                    d_i += 2
                elif dig[0][d_i + 1] > dig[1][p_i]:
                    if dig[0][d_i + 1] < dig[1][p_i + 1]:
                        raise Exception
                    else:
                        dig_count += dig[1][p_i + 1] - dig[0][d_i] + 1
                        dig[0].insert(d_i + 1, dig[1][p_i + 1] + 1)
                        for i in range(dig[0][d_i], dig[1][p_i + 1] + 1):
                            dig_cases.add((dig_index, i))
                        d_i += 1
                        p_i += 2
                else:
                    raise Exception

min_y = 555
min_x = 555
for x, y in dig_cases:
    if y < min_y:
        min_y = y
    if x < min_x:
        min_x = x
for y in range(min_y, 292 + min_y):
    for x in range(min_x, 304 + min_x):
        if (x, y) in dig_cases:
            print("#", end="")
        else:
            print(".", end="")
    print()
print(dig_count)
