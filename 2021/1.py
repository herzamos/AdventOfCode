def partOne():
    l = []
    with open("1.txt", "r") as f:
        for line in f.readlines():
            l.append(int(line))
    count = 0
    for i in range(1, len(l)):
        if (l[i] > l[i-1]):
            count+= 1
    print(count)

def partTwo():
    l = []
    with open("one.txt", "r") as f:
        for line in f.readlines():
            l.append(int(line))
    count = 0
    for i in range(1, len(l) - 2):
        if (l[i] + l[i+1] + l[i+2] > l[i-1] + l[i] + l[i+1]):
            count+= 1
    print(count)


if __name__ == "__main__":
    partOne()
    partTwo()