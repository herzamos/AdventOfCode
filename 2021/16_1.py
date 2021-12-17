def literal_to_number(packet):
    i = 6
    version, id = int(packet[:3], 2), int(packet[3:6], 2)
    literal = ""
    while (int(packet[i]) != 0):
        literal += packet[i+1:i+5]
        i += 5
    literal += packet[i+1:i+5]
    i += 5
    # return int(literal, 2)
    print(packet[:i])
    return version, i
    

def parse(packet):
    if len(packet) < 6:
        return 0, 0
    version, id = int(packet[:3], 2), int(packet[3:6], 2)
    if id == 4:
        return literal_to_number(packet)
    elif int(packet[6]) == 1:
        if len(packet) < 17:
            return 0, 0
        L = int(packet[7:18], 2)
        i = 18
        for _ in range(L):
            parsed = parse(packet[i:len(packet)])
            i += parsed[1]
            version += parsed[0]
        return version, i
    elif int(packet[6]) == 0:
        if len(packet) < 21:
            return 0, 0
        L = int(packet[7:22], 2)
        i, j = 22, 0
        while j < L:
            parsed = parse(packet[i:len(packet)])
            j += parsed[1]
            i += parsed[1]
            version += parsed[0]
        return version, i
    print("you should not be here")
    
    
with open("16.txt", "r") as f:
    packet = ""
    line = f.readline().strip("\n")
    for c in list(line):
        packet += str(bin(int(c, 16))[2:].zfill(4))
        
print(parse(packet))