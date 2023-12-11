class Node:
    def __init__(self, pos, previous_node):
        self.pos = pos
        self.previous_node = previous_node


grid = []
with open("input.txt") as file:
    for line in file:
        grid.append(line.strip())

S = Node((39, 50), None)

visited_nodes = {S.pos: 0}
step = 0
nodes_to_visit = [Node((40, 50), S)]
nodes_left = []
nodes_right = []
next_nodes_to_visit = []

while nodes_to_visit:

    step += 1
    for n in nodes_to_visit:
        visited_nodes[n.pos] = step
        next_pos = None
        if grid[n.pos[1]][n.pos[0]] == "|":
            if n.pos[1] - n.previous_node.pos[1] == 1:
                next_pos = (n.pos[0], n.pos[1] + 1)
                nodes_right.append((n.pos[0] - 1, n.pos[1]))
                nodes_left.append((n.pos[0] + 1, n.pos[1]))
            else:
                next_pos = (n.pos[0], n.pos[1] - 1)
                nodes_right.append((n.pos[0] + 1, n.pos[1]))
                nodes_left.append((n.pos[0] - 1, n.pos[1]))

        elif grid[n.pos[1]][n.pos[0]] == "-":
            if n.pos[0] - n.previous_node.pos[0] == 1:
                next_pos = (n.pos[0] + 1, n.pos[1])
                nodes_right.append((n.pos[0], n.pos[1] + 1))
                nodes_left.append((n.pos[0], n.pos[1] - 1))
            else:
                next_pos = (n.pos[0] - 1, n.pos[1])
                nodes_right.append((n.pos[0], n.pos[1] - 1))
                nodes_left.append((n.pos[0], n.pos[1] + 1))

        elif grid[n.pos[1]][n.pos[0]] == "L":
            if n.pos[1] - n.previous_node.pos[1] == 1:
                next_pos = (n.pos[0] + 1, n.pos[1])
                nodes_right.append((n.pos[0] - 1, n.pos[1]))
                nodes_right.append((n.pos[0] - 1, n.pos[1] + 1))
                nodes_right.append((n.pos[0], n.pos[1] + 1))
                nodes_left.append((n.pos[0] + 1, n.pos[1] - 1))
            else:
                next_pos = (n.pos[0], n.pos[1] - 1)
                nodes_left.append((n.pos[0] - 1, n.pos[1]))
                nodes_left.append((n.pos[0] - 1, n.pos[1] + 1))
                nodes_left.append((n.pos[0], n.pos[1] + 1))
                nodes_right.append((n.pos[0] + 1, n.pos[1] - 1))

        elif grid[n.pos[1]][n.pos[0]] == "J":
            if n.pos[1] - n.previous_node.pos[1] == 1:
                next_pos = (n.pos[0] - 1, n.pos[1])
                nodes_right.append((n.pos[0] - 1, n.pos[1] - 1))
                nodes_left.append((n.pos[0] + 1, n.pos[1]))
                nodes_left.append((n.pos[0] + 1, n.pos[1] + 1))
                nodes_left.append((n.pos[0], n.pos[1] + 1))
            else:
                next_pos = (n.pos[0], n.pos[1] - 1)
                nodes_left.append((n.pos[0] - 1, n.pos[1] - 1))
                nodes_right.append((n.pos[0] + 1, n.pos[1]))
                nodes_right.append((n.pos[0] + 1, n.pos[1] + 1))
                nodes_right.append((n.pos[0], n.pos[1] + 1))

        elif grid[n.pos[1]][n.pos[0]] == "7":
            if n.pos[1] - n.previous_node.pos[1] == -1:
                next_pos = (n.pos[0] - 1, n.pos[1])
                nodes_left.append((n.pos[0] - 1, n.pos[1] + 1))
                nodes_right.append((n.pos[0] + 1, n.pos[1]))
                nodes_right.append((n.pos[0] + 1, n.pos[1] - 1))
                nodes_right.append((n.pos[0], n.pos[1] - 1))
            else:
                next_pos = (n.pos[0], n.pos[1] + 1)
                nodes_right.append((n.pos[0] - 1, n.pos[1] + 1))
                nodes_left.append((n.pos[0] + 1, n.pos[1]))
                nodes_left.append((n.pos[0] + 1, n.pos[1] - 1))
                nodes_left.append((n.pos[0], n.pos[1] - 1))

        elif grid[n.pos[1]][n.pos[0]] == "F":
            if n.pos[1] - n.previous_node.pos[1] == -1:
                next_pos = (n.pos[0] + 1, n.pos[1])
                nodes_right.append((n.pos[0] + 1, n.pos[1] + 1))
                nodes_left.append((n.pos[0] - 1, n.pos[1]))
                nodes_left.append((n.pos[0] - 1, n.pos[1] - 1))
                nodes_left.append((n.pos[0], n.pos[1] - 1))

            else:
                next_pos = (n.pos[0], n.pos[1] + 1)
                nodes_left.append((n.pos[0] + 1, n.pos[1] + 1))
                nodes_right.append((n.pos[0] - 1, n.pos[1]))
                nodes_right.append((n.pos[0] - 1, n.pos[1] - 1))
                nodes_right.append((n.pos[0], n.pos[1] - 1))

        if next_pos not in visited_nodes:
            next_nodes_to_visit.append(Node(next_pos, n))
    nodes_to_visit.clear()
    nodes_to_visit.extend(next_nodes_to_visit)
    next_nodes_to_visit.clear()

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if (x,y) not in visited_nodes and (x,y) not in nodes_left and (x,y) not in nodes_right:
            if x != 0 and (x-1,y) in nodes_right :
                nodes_right.append((x,y))

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if (x, y) == (39, 50):
            print("S", end="")
        elif (x, y) in visited_nodes:
            print("#", end="")
        elif (x, y) in nodes_left:
            print("L", end="")
        elif (x, y) in nodes_right:
            print("R", end="")
        else:
            print(" ", end="")
    print()

nodes_right_inter = set(nodes_right).intersection(set(visited_nodes.keys()))
print(len(set(nodes_right))-len(nodes_right_inter))