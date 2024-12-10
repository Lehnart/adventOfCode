import enum
class Order(enum.Enum):
    ORDERED= 1
    NOT_ORDERED= 2
    MAYBE= 3

packets = []


with open("input.txt","r") as f:
    for line in f.readlines():
        if line.strip() == "":
            continue
        packets.append(eval(line))

def are_elements_in_order(el1,el2):
    if type(el1) == int and type(el2) == int :
        if el1 < el2 :
            return Order.ORDERED
        if el1 > el2 :
            return Order.NOT_ORDERED
        if el1 == el2 :
            return Order.MAYBE
    if type(el1) == int and type(el2) == list:
        return are_elements_in_order([el1], el2)
    if type(el1) == list and type(el2) == int:
        return are_elements_in_order(el1, [el2])
    if type(el1) == list and type(el2) == list:
        for index in range(len(el1)):
            subel1 = el1[index]
            if index >= len(el2):
                return Order.NOT_ORDERED
            subel2 = el2[index]
            is_ordered = are_elements_in_order(subel1, subel2)
            if is_ordered == Order.MAYBE :
                continue 
            return is_ordered
        return Order.ORDERED
    

def are_packets_in_order(p1, p2):
    for index in range(len(p1)):
        el1 = p1[index]

        if index >= len(p2):
            return Order.NOT_ORDERED

        el2 = p2[index]
        is_ordered = are_elements_in_order(el1, el2)
        if is_ordered == Order.MAYBE :
            continue 
        return is_ordered
    return Order.ORDERED

count = 0 
for packet_index in range(0, len(packets), 2):
    p1, p2 = packets[packet_index], packets[packet_index+1]
    is_ordered = are_packets_in_order(p1, p2)
    print(p1, p2, is_ordered)
    if is_ordered == Order.ORDERED:
        count += packet_index//2 + 1
print(count)