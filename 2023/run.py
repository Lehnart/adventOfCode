numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
calibration = 0
calibration2 = 0
with open("input.txt") as file :
    for line in file :
        line = line.strip()
        most_left_number = ""
        most_left_index = 10000

        most_right_number = ""
        most_right_index = -1

        for i, n in enumerate(numbers) :
            lfi = line.find(n)
            if lfi != -1 and lfi < most_left_index:
                most_left_number = n
                most_left_index = lfi

            rfi = line.rfind(n)
            if rfi != -1 and rfi > most_right_index:
                most_right_number = n
                most_right_index = rfi

        if most_left_index != 10000 :
            line = line.replace(most_left_number, str(numbers.index(most_left_number)+1)+most_left_number, 1)
        if most_right_index != -1:
            line = line[::-1].replace(most_right_number[::-1], most_right_number[::-1]+str(numbers.index(most_right_number)+1), 1)[::-1]

        digits = [c for c in line if c in "123456789"]
        calibration += int(digits[0]+digits[-1])

print(calibration)