page_array = []
for i in range(0,100):
    page_array.append([])
    for j in range(0,100):
        page_array[-1].append(True)

page_series = []

with open("input.txt","r") as f:
    for line in f.readlines():
        if "|" in line :
            left, right = line.split("|")
            page_array[int(right)][int(left)] = False 
        if "," in line :
            page_series.append([ int(page) for page in line.split(",")])
        

def is_ordered(page_line) :

    is_ordered = True 
    i_unordered = -1
    j_unordered = -1 

    for i in range(len(page_line)):
        if not is_ordered : 
            break 
        i_unordered = i 

        for j in range(i+1, len(page_line)):
            
            if not page_array[ page_line[i] ][page_line[j]] :
                is_ordered = False 

            j_unordered = j

            if not is_ordered :
                break 
            
    return is_ordered, i_unordered, j_unordered

def order(page_line):
    
    ordered = False 
    while not ordered :
        ordered, i, j = is_ordered(page_line)
        if i != -1 and j != -1 :
            page_line[i], page_line[j] = page_line[j], page_line[i]
        print(page_line)
    print()
    return page_line

count = 0
count_unordered = 0
for page_line in page_series:

    ordered, i , j = is_ordered(page_line)
            
    if ordered :
        count += page_line[len(page_line)//2]

    if not ordered :
        order_page_line = order(page_line)
        count_unordered += page_line[len(order_page_line)//2]

print(count)
print(count_unordered)