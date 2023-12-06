times = [38, 67, 76, 73]
distances = [234, 1027, 1157, 1236]
counts = [0, 0, 0, 0]

for i in range(len(times)):
    time_max, record = times[i], distances[i]
    for time_pressed in range(time_max):
        distance = time_pressed * (time_max - time_pressed)
        if distance > record:
            counts[i] += 1

print(counts[0] * counts[1] * counts[2] * counts[3])
