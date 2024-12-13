problem_array = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        if "+" in line :
            coordinates = line.strip().split(":")[1].split(",")
            moves = [int(m.split("+")[1]) for m in coordinates]
            problem_array.append(moves)
        elif ":" in line:
            coordinates = line.strip().split(":")[1].split(",")
            moves = [int(m.split("=")[1])+10**13 for m in coordinates]
            problem_array.append(moves)

total_cost = 0
for i in range(0, len(problem_array), 3):
    ax, ay = problem_array[i]
    bx, by = problem_array[i+1]
    x, y = problem_array[i+2]
    
    if ((x*by) - (y * bx)) % ((ax*by)-(bx*ay)) == 0:
        an = ((x*by) - (y * bx)) // ((ax*by)-(bx*ay))
        if (x - (an * ax))  % bx == 0 :
            bn = (x - (an * ax)) // bx
            print("an", an, "bn", bn)   
            if x != an*ax + bn*bx :
                print(x,y,an*ax + bn*bx, an*ay+bn*by)
            if y != an*ay+bn*by :
                print(x,y,an*ax + bn*bx, an*ay+bn*by)
            
            total_cost += bn + (3*an)
print(total_cost)