import itertools 
operations = []
with open("input.txt","r") as f:
    for line in f.readlines():
        result, operand_list_raw = line.strip().split(":")
        operands = [int(o) for o in operand_list_raw.split()]
        operations.append( (int(result), operands))
        
def compute(operands, operators):
    count = operands[0]
    for i in range(len(operators)):
        operator = operators[i]
        operand = operands[i+1]
        if operator == '*':
            count *= operand
        if operator == '+':
            count += operand 
        if operator == '|':
            count = int(str(count) + str(operand)) 

    return count 

count = 0
for result, operands in operations:
    operator_count = len(operands)-1
    for operator_combination in itertools.product('+*|', repeat=operator_count):
        if result == compute(operands, operator_combination):
            print (result, compute(operands, operator_combination), operator_combination)
            count += result
            break
print(count)