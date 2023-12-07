def find_number(x: int, y: int, rows, visited_cases):
    visited_cases.append((x, y))
    x_left = x - 1
    x_right = x + 1
    number_str = rows[y][x]
    while rows[y][x_left] in "0123456789":
        number_str = rows[y][x_left] + number_str
        visited_cases.append((x_left, y))
        x_left -= 1
    while x_right <= len(rows) - 1 and rows[y][x_right] in "0123456789":
        number_str = number_str + rows[y][x_right]
        visited_cases.append((x_right, y))
        x_right += 1
    return number_str


def main():
    rows = []
    gears_score = 0
    with open("input.txt") as file:
        for line in file:
            rows.append(line.strip())

    for y, row in enumerate(rows):
        for x, c in enumerate(row):
            if c != "*":
                continue

            numbers = []
            visited_cases = []
            if y > 0 and rows[y - 1][x] in "0123456789":
                numbers.append(find_number(x, y - 1, rows, visited_cases))

            if y < len(rows) - 1 and (x, y + 1) not in visited_cases and rows[y + 1][x] in "0123456789":
                numbers.append(find_number(x, y + 1, rows, visited_cases))

            if x > 0 and (x - 1, y) not in visited_cases and rows[y][x - 1] in "0123456789":
                numbers.append(find_number(x - 1, y, rows, visited_cases))

            if x < len(rows[y]) - 1 and (x + 1, y) not in visited_cases and rows[y][x + 1] in "0123456789":
                numbers.append(find_number(x + 1, y, rows, visited_cases))

            if y > 0 and x > 0 and (x - 1, y - 1) not in visited_cases and rows[y - 1][x - 1] in "0123456789":
                numbers.append(find_number(x - 1, y - 1, rows, visited_cases))

            if y > 0 and x < len(rows[y]) - 1 and (x + 1, y - 1) not in visited_cases and rows[y - 1][x + 1] in "0123456789":
                numbers.append(find_number(x + 1, y - 1, rows, visited_cases))

            if y < len(rows) - 1 and x > 0 and (x - 1, y + 1) not in visited_cases and rows[y + 1][x - 1] in "0123456789":
                numbers.append(find_number(x - 1, y + 1, rows, visited_cases))

            if y < len(rows) - 1 and x < len(rows[y]) - 1 and (x + 1, y + 1) not in visited_cases and rows[y + 1][x + 1] in "0123456789":
                numbers.append(find_number(x + 1, y + 1, rows, visited_cases))

            if len(numbers) == 2:
                gears_score += int(numbers[0]) * int(numbers[1])

    print(gears_score)


if __name__ == "__main__":
    main()
