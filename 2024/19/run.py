from functools import lru_cache
towels = []
designs = []
with open("input.txt","r") as f: 
    for line in f.readlines():
        if "," in line.strip():
            towels = tuple(line.strip().split(", "))

        elif line.strip():
            designs.append(line.strip())

print(towels)
print(designs)

@lru_cache(maxsize=1024)
def match_pattern(design, towels):
    count = 0
    for i in range(1, len(design)+1):
        if design[:i] in towels :
            if i == len(design):
                count += 1
            else :
                count += match_pattern(design[i:], towels)
    return count  

count = 0 
for design in designs :
    print(design)
    count += match_pattern(design, towels)
print(count)