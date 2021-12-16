import sys
import math

def literal_to_number(packet):
    i = 6
    literal = ""
    while (int(packet[i]) != 0):
        literal += packet[i+1:i+5]
        i += 5
    literal += packet[i+1:i+5]
    i += 5
    return int(literal, 2), i
    

def parse(packet):
    res = 0
    if len(packet) < 6:
        return 0, 0
    id = int(packet[3:6], 2)
    if id == 2:
        res = sys.maxsize
    if id == 1:
        res = 1
    if id == 4:
        return literal_to_number(packet)
    if int(packet[6]) == 1:
        if len(packet) < 17:
            return 0, 0
        L = int(packet[7:18], 2)
        i = 18
        for _ in range(L):
            parsed = parse(packet[i:])
            i += parsed[1]
            if id == 0:
                res += parsed[0]
            elif id == 1:
                res *= parsed[0]
            elif id == 2:
                res = min(res, parsed[0])
            elif id == 3:
                res = max(res, parsed[0])
            elif id == 5:
                first, j = parse(packet[18:])
                second, x = parse(packet[18+j:])
                res = 1 if first > second else 0
                return res, 18+j+x
            elif id == 6:
                first, j = parse(packet[18:])
                second, x = parse(packet[18+j:])
                res = 1 if first < second else 0
                return res, 18+j+x
            elif id == 7:
                first, j = parse(packet[18:])
                second, x = parse(packet[18+j:])
                res = 1 if first == second else 0
                return res, 18+j+x
        return res, i
    if int(packet[6]) == 0:
        if len(packet) < 21:
            return 0, 0
        L = int(packet[7:22], 2)
        i, j = 22, 0
        while j < L:
            parsed = parse(packet[i:])
            j += i - parsed[1]
            i += parsed[1]
            if id == 0:
                res += parsed[0]
            elif id == 1:
                res *= parsed[0]
            elif id == 2:
                res = min(res, parsed[0])
            elif id == 3:
                res = max(res, parsed[0])
            elif id == 5:
                first, j = parse(packet[22:])
                second, x = parse(packet[22+j:])
                res = 1 if first > second else 0
                return res, 22+j+x
            elif id == 6:
                first, j = parse(packet[22:])
                second, x = parse(packet[22+j:])
                res = 1 if first < second else 0
                return res, 22+j+x
            elif id == 7:
                first, j = parse(packet[22:])
                second, x = parse(packet[22+j:])
                res = 1 if first == second else 0
                return res, 22+j+x
        return res, i
    
    
with open("16.txt", "r") as f:
    packet = ""
    line = f.readline().strip("\n")
    for c in list(line):
        packet += str(bin(int(c, 16))[2:].zfill(4))
print(packet)
print(len(packet))
print(parse(packet))