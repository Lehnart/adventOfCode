with open("input.txt") as file:
    msg = file.readline()
    for i in range(0, len(msg)-5):
        marker = msg[i:i+4]
        if len(set(marker)) == len(marker) :
            print(i+4)
            break
    for i in range(0, len(msg)-5):
        marker = msg[i:i + 14]
        if len(set(marker)) == len(marker):
            print(i + 14)
            break