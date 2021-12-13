def partOne(steps):
    a = []
    with open("11.txt", "r") as f:
        for line in f.readlines():
            a.append(list(map(int, list(line.strip("\n")))))
    flashed = [[False for i in range(10)] for j in range(10)]
    flashes = 0
    for c in range(steps):
        for i in range(len(a)):
            for j in range(len(a[0])):
                a[i][j] += 1
        for i in range(len(a)):
            for j in range(len(a[0])):
                if a[i][j] >= 10 and not flashed[i][j]:
                    flashed[i][j] = True
                    flash(a, i, j, flashed)
        for i in range(len(a)):
            for j in range(len(a[0])):
                if a[i][j] >= 10:
                    a[i][j] = 0
                if flashed[i][j]:
                    flashed[i][j] = False
                    flashes += 1
    print(flashes)
        
def partTwo():
    a = []
    with open("eleven.txt", "r") as f:
        for line in f.readlines():
            a.append(list(map(int, list(line.strip("\n")))))
    flashed = [[False for i in range(10)] for j in range(10)]
    flashes = 0
    c = 0
    while True:
        for i in range(len(a)):
            for j in range(len(a[0])):
                a[i][j] += 1
        for i in range(len(a)):
            for j in range(len(a[0])):
                if a[i][j] >= 10 and not flashed[i][j]:
                    flashed[i][j] = True
                    flash(a, i, j, flashed)
        for i in range(len(a)):
            for j in range(len(a[0])):
                if a[i][j] >= 10:
                    a[i][j] = 0
                if flashed[i][j]:
                    flashed[i][j] = False
                    flashes += 1
        c += 1
        if flashes == 100:
            return c
        flashes = 0
            
def flash(a, i, j, flashed):
    for (k, l) in adjacentIndices(i, j, len(a), len(a[0])):
        a[k][l] += 1
    for (k, l) in adjacentIndices(i, j, len(a), len(a[0])):
        if a[k][l] >= 10 and not flashed[k][l]:
            flashed[k][l] = True
            flash(a, k, l, flashed)


def adjacentIndices(i, j, m, n):
    adjacent_indices = []
    if i > 0:
        adjacent_indices.append((i-1,j))
        if j > 0:
            adjacent_indices.append((i-1,j-1))
    if i+1 < m:
        adjacent_indices.append((i+1,j))
        if j + 1 < n:
            adjacent_indices.append((i+1,j+1))
    if j > 0:
        adjacent_indices.append((i,j-1))
        if i+1 < m:
            adjacent_indices.append((i+1,j-1))
    if j+1 < n:
        adjacent_indices.append((i,j+1))
        if i > 0:
            adjacent_indices.append((i-1,j+1))
    return adjacent_indices


if __name__ == "__main__":
    partOne(100)
    print(partTwo())