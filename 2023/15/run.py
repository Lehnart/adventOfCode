def ascii_hash(s):
    current_value = 0
    for c in s:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value

with open("input.txt") as file:
    lines = file.readlines()
line = lines[0].strip()
som = 0
for string in line.split(","):
    current_value = ascii_hash(string)
    som += current_value
print(som)