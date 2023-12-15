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
boxes = [[] for _ in range(256)]
for string in line.split(","):
    if "=" in string:
        label, n = string.split("=")
        focal_length = int(n)
        box = ascii_hash(label)
        labels_in_box = [b[0] for b in boxes[box]]
        if label in labels_in_box:
            for i in range(len(boxes[box])):
                if boxes[box][i][0] == label:
                    boxes[box][i][1] = focal_length
                    break
        else:
            boxes[box].append([label, focal_length])
    elif "-" in string:
        label = string.split("-")[0]
        box = ascii_hash(label)
        labels_in_box = [b[0] for b in boxes[box]]
        if label in labels_in_box:
            for i in range(len(boxes[box])):
                if boxes[box][i][0] == label:
                    boxes[box].pop(i)
                    break

focusing_power = 0
for box_index, box in enumerate(boxes):
    box_focusing_power = (1+box_index)
    for lens_index, lens in enumerate(box):
        lens_power = box_focusing_power*(1+lens_index)*lens[1]
        focusing_power += lens_power
print(focusing_power)