from os import system, name
import sys
import time

def partTwoAnimation():
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
        return
    colorMap[i][j] = color
    colored[i][j] = True
    drawMap(height, colored)
    for (k, l) in adjacentIndices(i, j, len(height), len(height[0])):
        colorAdjacent(k, l, height, color, colorMap, colored)
        
def drawMap(height, colored):
    clear()
    toPrint = ""
    for i in range(len(height)):
        for j in range(len(height[0])):
            if colored[i][j]:
                if height[i][j] == 9:
                    toPrint += u"\u001b[48;5;14m 9"
                elif 6 <= height[i][j] <= 8:
                    toPrint += u"\u001b[48;5;33m " + str(height[i][j])
                elif 3 <= height[i][j] <= 5:
                    toPrint += u"\u001b[48;5;31m " + str(height[i][j])
                else:   
                    toPrint += u"\u001b[48;5;26m " + str(height[i][j])
            else:
                if height[i][j] == 9:
                    toPrint += u"\u001b[48;5;238m 9"
                elif 6 <= height[i][j] <= 8:
                    toPrint += u"\u001b[48;5;242m " + str(height[i][j])
                elif 3 <= height[i][j] <= 5:
                    toPrint += u"\u001b[48;5;246m " + str(height[i][j])
                else:   
                    toPrint += u"\u001b[48;5;250m " + str(height[i][j])
        toPrint += "\n"
    sys.stdout.write(toPrint)
        
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
        

if __name__ == "__main__":
    partTwoAnimation()
    
