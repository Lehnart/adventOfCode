times = [38677673]
distances = [234102711571236]
counts = [0, 0, 0, 0]

for i in range(len(times)):
    time_max, record = times[i], distances[i]
    for time_pressed in range(time_max):
        distance = time_pressed * (time_max - time_pressed)
        if distance > record:
            counts[i] += 1

print(counts[0])

