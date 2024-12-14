robots = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        p, v = line.split(" ")
        x,y = [ int(c) for c in p.split("=")[1].split(",")]
        vx,vy = [ int(c) for c in v.split("=")[1].split(",")]
        robots.append((x,y,vx,vy))

width = 101 
height = 103
for t in range(28,10000,101):
    next_robot_positions = []
    grid = [[" " for _ in range(width)] for _ in range(height)]
    for robot in robots:
        x,y,vx,vy = robot 
        nx = (x + (vx*t))%width
        ny = (y + (vy*t))%height
        next_robot_positions.append((nx,ny))
        grid[ny][nx] = "X"

    q1,q2,q3,q4 = 0,0,0,0
    for next_position in next_robot_positions:
        x, y = next_position
        if x < width // 2 and y < height // 2 :
            q1 += 1 
        if x > width // 2 and y < height // 2 :
            q2 += 1 
        if x < width // 2 and y > height // 2 :
            q3 += 1 
        if x > width // 2 and y > height // 2 :
            q4 += 1 
   
    if q1 <  50 or q2 < 50 or q3 < 50 or q4 < 50 : 
        print (t, q1,q2,q3,q4)
        with open("output_"+str(t)+".txt", "w") as f:
            for row in grid:
                for col in row:
                    f.write(col)
                f.write("\n")    

print(q1*q2*q3*q4)