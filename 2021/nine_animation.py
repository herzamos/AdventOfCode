import os

palette = [[u"\u001b[48;5;17m ", ]]

def partTwoAnimation():
    os.system('cls' if os.name == 'nt' else 'clear')
    height = []
    isRisk = []
    colorMap = []
    colored = []
    color = 1
    with open("nine.txt", "r") as f:
        for line in f.readlines():
            height.append(list(map(int, list(line.strip("\n")))))
            isRisk.append([True for i in range(len(line))])
            colorMap.append([0 for i in range(len(line))])
            colored.append([False for i in range(len(line))])
    drawMap(height, colored)
    for i in range(len(height)):
        for j in range(len(height[0])):
            for (k, l) in adjacentIndices(i, j, len(height), len(height[0])):
                isRisk[i][j] = (True and isRisk[i][j]) if height[i][j] < height[k][l] else False
    for i in range(len(height)):
        for j in range(len(height[0])):
            if isRisk[i][j]:
                colorAdjacent(i, j, height, color, colorMap, colored)
                color += 1

def adjacentIndices(i, j, m, n):
    adjacent_indices = []
    if i > 0:
        adjacent_indices.append((i-1,j))
    if i+1 < m:
        adjacent_indices.append((i+1,j))
    if j > 0:
        adjacent_indices.append((i,j-1))
    if j+1 < n:
        adjacent_indices.append((i,j+1))
    return adjacent_indices


def colorAdjacent(i, j, height, color, colorMap, colored):
    if colorMap[i][j] != 0:
        return
    if height[i][j] == 9:
        colored[i][j] = True
        drawMap(height, colored)
        return
    colorMap[i][j] = color
    colored[i][j] = True
    drawMap(height, colored)
    for (k, l) in adjacentIndices(i, j, len(height), len(height[0])):
        colorAdjacent(k, l, height, color, colorMap, colored)
        
def drawMap(height, colored):
    toPrint = ""
    for i in range(len(height)):
        for j in range(len(height[0])):
            if colored[i][j]:
                if height[i][j] == 9:
                    toPrint += u"\u001b[48;5;16m " + str(height[i][j])
                elif 7 <= height[i][j] <= 8:
                    toPrint += u"\u001b[48;5;196m " + str(height[i][j])
                elif 4 <= height[i][j] <= 6:
                    toPrint += u"\u001b[48;5;202m " + str(height[i][j])
                elif height[i][j] == 3:
                    toPrint += u"\u001b[48;5;220m " + str(height[i][j])
                else:   
                    toPrint += u"\u001b[48;5;228m " + str(height[i][j])
            else:
                if height[i][j] == 9:
                    toPrint += u"\u001b[48;5;16m 9"
                elif 7 <= height[i][j] <= 8:
                    toPrint += u"\u001b[48;5;240m " + str(height[i][j])
                elif 4 <= height[i][j] <= 6:
                    toPrint += u"\u001b[48;5;242m " + str(height[i][j])
                elif height[i][j] == 3:
                    toPrint += u"\u001b[48;5;244m " + str(height[i][j])
                else:   
                    toPrint += u"\u001b[48;5;246m " + str(height[i][j])
        toPrint += "\n"
    print(toPrint)
    print(u"\033[0;0Hm")

if __name__ == "__main__":
    partTwoAnimation()
    
