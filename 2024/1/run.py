import os 

os.chdir("/home/thomas.serre/Perso/adventOfCode/2024/1")

l1, l2 = [], []
with open("input.txt","r") as f:
    for line in f.readlines():
        el1, el2 = line.split()
        l1.append(int(el1))
        l2.append(int(el2))
l1.sort()
l2.sort()
print(l1)
print(l2)
distances = [ abs(l1[i] - l2[i]) for i in range(len(l1))]
print("sol1 ", sum(distances))

counter = {}
for el2 in l2 :
    if el2 not in counter:
        counter[el2] = 0 
    counter[el2] += 1

count = 0 
for el1 in l1 :
    if el1 not in counter :
        continue 
    count += el1 * counter[el1]

print("sol2 ", count)