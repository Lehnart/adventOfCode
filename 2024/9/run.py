raw_memory = None
with open("input.txt","r") as f:
    raw_memory = f.read().strip()

def find_largest_void(memory):
    start_void = False 
    current_size = 0 
    max_size = 0
    for c in memory :
        if c == '.':
            if not start_void:
                start_void = True 
            current_size += 1
        else :
            if start_void :
                max_size = current_size if current_size > max_size else max_size
                start_void = False 
                current_size = 0 
    return max_size

def find_first_void(memory, min_size, max_index):
    start_void = False 
    current_size = 0 
    for index, c in enumerate(memory[:max_index+1]) :
        if c == '.':
            if not start_void:
                start_void = True 
            current_size += 1
        else :
            if start_void and current_size >= min_size : 
                return index - current_size
            current_size = 0 
    return None 

def get_file_size(memory, file_id, right_index):
    current_index = right_index 
    file_size = 0
    while(current_index < len(memory) and memory[current_index] == file_id):
        file_size += 1
        current_index -= 1 
    return file_size 

def find_last_unordered_file(raw_memory, last_index):
    reversed_memory = raw_memory[last_index::-1]
    for index, c in enumerate(reversed_memory):
        if c == '.':
            continue
        else :
            file_id = c
            file_size = 0
            while index < len(reversed_memory) and reversed_memory[index] == file_id:
                file_size += 1
                index += 1 
            return file_id, file_size, len(reversed_memory) - 1 - index + 1 

def move_file(memory, file_tuple, void_index):
    _, file_size, file_index =  file_tuple
    for i in range(file_size):
        memory[void_index+i], memory[file_index+i] = memory[file_index+i], memory[void_index+i]


def part1 (raw_memory):
    memory = []
    free_memory_indices = []
    
    is_file = True 
    file_id = 0
    for c in raw_memory:
        element_to_add = str(file_id) if is_file else '.'
        for _ in range(int(c)):
            memory.append(element_to_add)
            free_memory_indices.append( False if is_file else True )
        is_file = not is_file
        if is_file : 
            file_id += 1


    last_index = len(memory) - 1 
    max_file_id, _, _ = find_last_unordered_file(memory, last_index)
    ordered_file_ids = set()
    while not len(ordered_file_ids) == int(max_file_id) + 1:
        file_id, file_size, file_index = find_last_unordered_file(memory, last_index)   
        last_index = file_index - 1 
        print(file_id, file_size, file_index )
        if file_id in ordered_file_ids:
            continue
        ordered_file_ids.add(file_id)
        void_index= find_first_void(memory, file_size, file_index)
        
        if void_index is None :
            continue 
        move_file(memory, (file_id, file_size, file_index), void_index)
        
    checksum = 0
    for i, el in enumerate(memory):
        if el == ".":
            continue
        checksum += int(el)*i
    print(checksum)

part1(raw_memory)