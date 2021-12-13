import sys

def partOne():
    crabs = []
    with open("7.txt", "r") as f:
        crabs = list(map(int, f.readline().strip("\n").split(",")))
    m = max(crabs)
    minFuel = sys.maxsize
    for i in range(m):
        fuel = 0
        for crab in crabs:
            fuel += abs(i - crab)
        minFuel = fuel if fuel < minFuel else minFuel
    print(minFuel)
    
def partTwo():
    crabs = []
    with open("seven.txt", "r") as f:
        crabs = list(map(int, f.readline().strip("\n").split(",")))
    m = max(crabs)
    minFuel = sys.maxsize
    for i in range(m):
        fuel = 0
        for crab in crabs:
            fuel += gauss(abs(i - crab))
        minFuel = fuel if fuel < minFuel else minFuel
    print(minFuel)
    
def gauss(n):
    return (n * (n + 1)) / 2

if __name__ == "__main__":
    partOne()
    partTwo()