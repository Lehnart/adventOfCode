with open("input.txt") as file:
    lines = file.readlines()

directions = lines[0].strip()
nodes = {}
for line in lines[2:]:
    node, raw_next_nodes = line.strip().replace(" ", "").split("=")
    next_nodes = raw_next_nodes.strip().replace(" ", "").replace("(", "").replace(")", "").split(",")
    if node in nodes:
        raise Exception
    nodes[node] = next_nodes

steps = []
current_nodes = [n for n in nodes.keys() if n[2] == "A"]
for current_node in current_nodes :
    print(current_node)
    next_instruction_index = 0
    step_count = 0
    end_nodes = []
    end_steps = []
    while current_node[2] != "Z" or current_node not in end_nodes:
        if current_node[2] == "Z" :
            end_nodes.append(current_node)
            end_steps.append(step_count)
        next_instruction = directions[next_instruction_index%len(directions)]
        next_instruction_index += 1
        step_count +=1
        if next_instruction == "R" :
            current_node = nodes[current_node][1]
        elif next_instruction == "L" :
            current_node = nodes[current_node][0]
        else:
            raise Exception
    steps.append(end_steps[0])
    print(end_steps)
    print(end_nodes)
print(steps)
min_step = min(steps)
result = 52243757257*263
print(result)
for s in steps :
    print(result%s)