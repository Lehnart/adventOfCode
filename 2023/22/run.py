MAX_CUBE = 325
grid = [[[0 for _ in range(MAX_CUBE)] for _ in range(MAX_CUBE)] for _ in range(MAX_CUBE)]
brick_id_to_positions = {}
with open("input.txt") as file:
    brick_id = 1
    for line in file:
        raw_brick_start, raw_brick_end = line.strip().split("~")
        brick_start = [int(c) for c in raw_brick_start.split(",")]
        brick_end = [int(c) for c in raw_brick_end.split(",")]
        brick_id_to_positions[brick_id] = []

        x0, y0, z0 = brick_start
        x1, y1, z1 = brick_end
        if x0 != x1:
            for x in range(min(x0, x1), max(x0, x1) + 1):
                grid[z0][y0][x] = brick_id
                brick_id_to_positions[brick_id].append((x, y0, z0))
        elif y0 != y1:
            for y in range(min(y0, y1), max(y0, y1) + 1):
                grid[z0][y][x0] = brick_id
                brick_id_to_positions[brick_id].append((x0, y, z0))
        elif z0 != z1:
            for z in range(min(z0, z1), max(z0, z1) + 1):
                grid[z][y0][x0] = brick_id
                brick_id_to_positions[brick_id].append((x0, y0, z))
        else:
            grid[z0][y0][x0] = brick_id
            brick_id_to_positions[brick_id].append((x0, y0, z0))
        brick_id += 1

brick_id_max = brick_id
min_z_and_ids = []
for brick_id in range(1, brick_id_max):
    if len([z for _, _, z in brick_id_to_positions[brick_id]]) == 0:
        print()
    min_z_and_ids.append((brick_id, min(z for _, _, z in brick_id_to_positions[brick_id])))
min_z_and_ids.sort(key=lambda k: k[1])

for brick_id, _ in min_z_and_ids:
    zs = []
    for x, y, z in brick_id_to_positions[brick_id]:
        current_z = z
        while True:
            under_brick_id = grid[current_z][y][x]
            if under_brick_id not in [0, brick_id] or current_z == 0:
                zs.append((z - current_z - 1))
                break
            current_z -= 1
    z_move = min(zs)
    if z_move == 0:
        continue
    next_positions = []
    for x, y, z in brick_id_to_positions[brick_id]:
        next_positions.append((x, y, z - z_move))
        grid[z][y][x] = 0
        grid[z - z_move][y][x] = brick_id

    brick_id_to_positions[brick_id] = list(next_positions)

brick_support_map = {0: set()}
brick_supported_map = {}
for id in range(1, brick_id_max):
    if any(z == 1 for _, _, z in brick_id_to_positions[id]):
        brick_support_map[0].add(id)
        continue
    for x, y, z in brick_id_to_positions[id]:
        support = grid[z - 1][y][x]
        if support == 0 or support == id:
            continue
        if support not in brick_support_map:
            brick_support_map[support] = set()
        if id not in brick_supported_map:
            brick_supported_map[id] = set()
        brick_support_map[support].add(id)
        brick_supported_map[id].add(support)

print(brick_support_map)
print(brick_supported_map)
destroyable_bricks = []
for brick_id in range(1, brick_id_max):
    if brick_id not in brick_support_map:
        destroyable_bricks.append(brick_id)
        continue
    if all(len(brick_supported_map[supported_brick]) > 1 for supported_brick in brick_support_map[brick_id]):
        destroyable_bricks.append(brick_id)

fall_counts = []
for destroyed_brick_id in range(1, brick_id_max):
    destroyed_bricks = set()
    destroyed_bricks.add(destroyed_brick_id)
    nexts_to_fall = set()
    nexts_to_fall.add(destroyed_brick_id)
    while nexts_to_fall :
        nexts_to_fall.clear()
        for brick_id in range(1, brick_id_max):
            if brick_id in destroyed_bricks:
                continue
            if brick_id not in brick_supported_map:
                continue
            if all(b in destroyed_bricks for b in brick_supported_map[brick_id]):
                if brick_id not in destroyed_bricks:
                    nexts_to_fall.add(brick_id)
        destroyed_bricks = destroyed_bricks.union(nexts_to_fall)
    fall_counts.append(len(destroyed_bricks)-1)
print(sum(fall_counts))