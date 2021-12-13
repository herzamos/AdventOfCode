def partOne():
    map = [[0 for x in range(1000)] for y in range(1000)]
    coord1 = []
    coord2 = []
    ret = 0
    with open("5.txt", "r") as f:
        for line in f.readlines():
            coords = line.strip("\n").split(" -> ")
            coord1.append([int(x) for x in coords[0].split(",")])
            coord2.append([int(x) for x in coords[1].split(",")])
    for i in range(len(coord1)):
        x1 = coord1[i][0]
        x2 = coord2[i][0]
        y1 = coord1[i][1]
        y2 = coord2[i][1]
        if x1 == x2:
            for j in range(min(y1, y2), max(y1 + 1, y2 + 1)):
                map[j][x1] += 1
        elif y1 == y2:
            for j in range(min(x1, x2), max(x1 + 1, x2 + 1)):
                map[y1][j] += 1
    for row in map:
        for e in row:
            if e >= 2:
                ret += 1
    print(ret)
    
def partTwo():
    map = [[0 for x in range(1000)] for y in range(1000)]
    coord1 = []
    coord2 = []
    ret = 0
    with open("five.txt", "r") as f:
        for line in f.readlines():
            coords = line.strip("\n").split(" -> ")
            coord1.append([int(x) for x in coords[0].split(",")])
            coord2.append([int(x) for x in coords[1].split(",")])
    for i in range(len(coord1)):
        x1 = coord1[i][0]
        x2 = coord2[i][0]
        y1 = coord1[i][1]
        y2 = coord2[i][1]
        if x1 == x2:
            for j in range(min(y1, y2), max(y1 + 1, y2 + 1)):
                map[j][x1] += 1
        elif y1 == y2:
            for j in range(min(x1, x2), max(x1 + 1, x2 + 1)):
                map[y1][j] += 1
        else:
            if x1 < x2 and y1 < y2:
                while x1 <= x2:
                    map[y1][x1] += 1
                    x1 += 1
                    y1 += 1
            elif x1 < x2 and y1 > y2:
                while x1 <= x2:
                    map[y1][x1] += 1
                    x1 += 1
                    y1 -= 1
            elif x1 > x2 and y1 < y2:
                while x1 >= x2:
                    map[y1][x1] += 1
                    x1 -= 1
                    y1 += 1
            elif x1 > x2 and y1 > y2:
                while x1 >= x2:
                    map[y1][x1] += 1
                    x1 -= 1
                    y1 -= 1
    for row in map:
        for e in row:
            if e >= 2:
                ret += 1
    print(ret)

if __name__ == "__main__":
    partOne()
    partTwo()