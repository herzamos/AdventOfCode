def printMap(map):
    for line in map:
        for i in range(len(line)):
            if line[i]: print("#", end = "")
            else: print(".", end = "")
        print()
        
def fold(paper, vertical, coord):
    if vertical:
        for i in range(coord, len(paper)):
            for j in range(len(paper[0])):
                if paper[i][j]:
                    paper[2*coord - i][j] = True
        paper = paper[:coord]
    else:  
        for i in range(len(paper)):
            for j in range(coord, len(paper[0])):
                if paper[i][j]:
                    paper[i][2*coord - j] = True
        for i in range(len(paper)):
            paper[i] = paper[i][:coord]
    return paper

points = []
coords = []

with open("13.txt", "r") as f:
    for line in f.readlines():
        if len(line.strip("\n").split("=")) != 1:
            coords.append((line.strip("\n").split("=")[0][-1], int(line.strip("\n").split("=")[1])))
        elif len(line.strip("\n").split(",")) == 2:
            points.append(tuple(map(int, list(line.strip().split(",")))))
maxy, maxx = 0, 0
for i in range(len(points)):
    maxy = points[i][1] if points[i][1] > maxy else maxy
    maxx = points[i][0] if points[i][0] > maxx else maxx

map = [[False for x in range(maxx + 1)] for y in range(maxy + 1)]

for i in range(len(points)):
    map[points[i][1]][points[i][0]] = True
    
## PART ONE ##
vertical = True if coords[0][0] == "y" else False
coord = coords[0][1]
sum = 0
newMap = fold(map, vertical, coord)
for line in newMap:
    for i in range(len(line)):
        sum += 1 if line[i] else 0
print(sum)

## PART TWO ##
for c in coords:
    vertical = True if c[0] == "y" else False
    coord = c[1]
    map = fold(map, vertical, coord)
    
printMap(map)