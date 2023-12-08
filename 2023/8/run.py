with open("input.txt") as file:
    lines = file.readlines()

directions = lines[0].strip()
nodes = {}
for line in lines[2:]:
    node, raw_next_nodes = line.strip().replace(" ", "") .split("=")
    next_nodes = raw_next_nodes.strip().replace(" ", "").replace("(", "").replace(")", "").split(",")
    if node in nodes:
        raise Exception
    nodes[node] = next_nodes

current_node = "AAA"
next_instruction_index = 0
step_count = 0
while current_node != "ZZZ" :
    next_instruction = directions[next_instruction_index%len(directions)]
    next_instruction_index += 1
    step_count +=1
    if next_instruction == "R" :
        current_node = nodes[current_node][1]
    elif next_instruction == "L" :
        current_node = nodes[current_node][0]
    else:
        raise Exception
print(step_count)