raw_connections = []
with open("input.txt","r") as f :
    for line in f.readlines():
        a,b=line.strip().split("-")
        raw_connections.append((a,b))

connections = {}
for c1,c2 in raw_connections:
    
    if c1 not in connections:
        connections[c1] = set()
    connections[c1].add(c2)
    
    if c2 not in connections:
        connections[c2] = set()
    connections[c2].add(c1)

connectedsss = {}
count = 0
for key1 in connections.keys():
    connections1 = connections[key1]
    for key2 in connections[key1]:
        connections2 = connections[key2]
        co1 = set(connections1)
        co2 = set(connections2)
        co1.remove(key2)
        co2.remove(key1)
#        print(co1, co2)
        if( len(co1.intersection(co2)) ) == 11 :
            inter = list(co1.intersection(co2))
            is_co = True 
            for i in range(0,len(inter)):
                n1 = inter[i]
                if not is_co : 
                    break
                for j in range(i+1, len(inter)):
                    n2 = inter[j]
                    if n1 not in connections[n2]:
                        is_co = False 
                        break 
            if is_co :
                count += 1 
                print("CONECTEd")
                print(key1, key2, inter)
print(count)

l = list(set(["km", "jc", 'sx', 'wq', 'hz', 'wc', 'mv', 'xy', 'sv', 'ei', 'az', 'kt', 'cg']))
l.sort()
print(",".join(l))
# connected_5 = set()
# for key in connections.keys():
#     cs = list(connections[key])
#     for i in range(0,len(cs)):
#         c1 = cs[i]
#         for j in range(i+1,len(cs)):
#             c2 = cs[j]
#             for k in range(j+1,len(cs)):
#                 c3 = cs[k]
#                 for l in range(k+1,len(cs)):
#                     c4 = cs[l]

#                     if c2 in connections[c1] and c2 in connections[c3] and c2 in connections[c4] and c2 in connections[c5] :
#                         l = [key,c1,c2]
#                         l.sort()
#                         connected_3.add(tuple(l))

# quads = set()
# for triangle in connected_3: 
#     for key in connections.keys():
#         if key in triangle : 
#             continue 
#         cos = connections[key]
#         is_connected = True  
#         for t in triangle :
#             if t not in cos :
#                 is_connected = False 
#                 break 
#         if is_connected :
#             l = [*triangle, key]
#             l.sort()
#             quads.add(tuple(l))
# for q in quads:
#     print(q) 
# print(len(connected_3))
# print(len(quads))
# count_key = 0 
# count_co = 0 
# for key in connections:
#     count_key += 1
#     count_co += len(connections[key])

