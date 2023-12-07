def is_next_to_symbol(c, x, y, rows):
    if c not in "0123456789":
        return False

    if y > 0 and rows[y - 1][x] not in "0123456789.":
        return True

    if y < len(rows) - 1 and rows[y + 1][x] not in "0123456789.":
        return True

    if x > 0 and rows[y][x - 1] not in "0123456789.":
        return True

    if x < len(row) - 1 and rows[y][x + 1] not in "0123456789.":
        return True

    if y > 0 and x > 0 and rows[y - 1][x - 1] not in "0123456789.":
        return True

    if y > 0 and x < len(row) - 1 and rows[y - 1][x + 1] not in "0123456789.":
        return True

    if y < len(rows) - 1 and x > 0 and rows[y + 1][x - 1] not in "0123456789.":
        return True

    if y < len(rows) - 1 and x < len(row) - 1 and rows[y + 1][x + 1] not in "0123456789.":
        return True

    return False


rows = []
part_number_sum = 0
is_treated = []

with open("input.txt") as file:
    for line in file:
        rows.append(line.strip())

x_rights = []
for y, row in enumerate(rows):
    for x, c in enumerate(row):
        if x in x_rights:
            x_rights.pop(0)
            continue
        if not is_next_to_symbol(c, x, y, rows):
            continue

        part_number_str = c
        x_left = x - 1
        x_right = x + 1
        while x_left >= 0 and row[x_left] in "0123456789":
            part_number_str = row[x_left] + part_number_str
            x_left -= 1
        while x_right <= len(row) - 1 and row[x_right] in "0123456789":
            part_number_str = part_number_str + row[x_right]
            x_rights.append(x_right)
            x_right += 1

        part_number = int(part_number_str)
        part_number_sum += part_number
print(part_number_sum)