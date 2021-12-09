def partOne():
    height = []
    isRisk = []
    sum = 0
    with open("nine.txt", "r") as f:
        for line in f.readlines():
            height.append(list(map(int, list(line.strip("\n")))))
            isRisk.append([True for i in range(len(line))])
    for i in range(len(height)):
        for j in range(len(height[0])):
            for (k, l) in adjacentIndices(i, j, len(height), len(height[0])):
                isRisk[i][j] = (True and isRisk[i][j]) if height[i][j] < height[k][l] else False
    for i in range(len(height)):
        for j in range(len(height[0])):
            if isRisk[i][j]:
                sum += height[i][j] + 1
    print(sum)
    
    
def partTwo():
    height = []
    isRisk = []
    colorMap = []
    color = 1
    with open("nine.txt", "r") as f:
        for line in f.readlines():
            height.append(list(map(int, list(line.strip("\n")))))
            isRisk.append([True for i in range(len(line))])
            colorMap.append([0 for i in range(len(line))])
    for i in range(len(height)):
        for j in range(len(height[0])):
            for (k, l) in adjacentIndices(i, j, len(height), len(height[0])):
                isRisk[i][j] = (True and isRisk[i][j]) if height[i][j] < height[k][l] else False
    for i in range(len(height)):
        for j in range(len(height[0])):
            if isRisk[i][j]:
                colorAdjacent(i, j, height, color, colorMap)
                color += 1
                
    colorCount = [0 for i in range(color+1)]
    for i in range(len(height)):
        for j in range(len(height[0])):
            colorCount[colorMap[i][j]] += 1
    colorCount[0] = 0
    colorCount = sorted(colorCount, reverse=True)
    print(colorCount[0] * colorCount[1] * colorCount[2])
    

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


def colorAdjacent(i, j, height, color, colorMap):
    if colorMap[i][j] != 0:
        return
    if height[i][j] == 9:
        return
    colorMap[i][j] = color
    for (k, l) in adjacentIndices(i, j, len(height), len(height[0])):
        colorAdjacent(k, l, height, color, colorMap)

if __name__ == "__main__":
    partOne()
    partTwo()