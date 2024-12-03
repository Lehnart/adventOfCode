memory= ""
with open("input.txt","r") as f:
    memory = f.read()


muls = []
is_do = True 
for i in range(len(memory)):

    if memory[i:].startswith("do()"):
        is_do = True 
        continue 
        
    if memory[i:].startswith("don't()"):
        is_do = False 
        continue 

    if not is_do :
        continue 

    if memory[i:i+4] != "mul(":
        continue 
    if memory[i+4] not in "0123456789":
        continue

    reached_comma = False
    j = i+4
    while True :
        if memory[j] not in "0123456789":
            if memory[j] == ",":
                reached_comma=True 
            break 
        j+=1

    if not reached_comma:
        continue

    if memory[j+1] not in "0123456789":
        continue
    
    reached_parenthesis = False
    k = j+1
    while True :
        if memory[k] not in "0123456789":
            if memory[k] == ")":
                reached_parenthesis=True 
            break 
        k+=1
    
    if not reached_parenthesis:
        continue
    
    muls.append(memory[i:k+1])

count = 0
for mul in muls:
    op1, op2 = mul[mul.index("(")+1: mul.index(")")].split(",")
    op1 = int(op1)
    op2 = int(op2)
    count += op1*op2
print(count)