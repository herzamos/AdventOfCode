def partOne(days):
    with open("six.txt", "r") as f:
        fishes = list(map(int, f.readline().strip("\n").split(",")))
    for i in range(1, days+1):
        for j in range(len(fishes)):
            if fishes[j] == 0:
                fishes[j] = 6
                fishes.append(8)
                continue
            fishes[j] -= 1
    print("After {} days: {} fishes".format(256, len(fishes)))
    
def partTwo(days):
    curr = [[0 for x in range(9)] for y in range(days+2)]
    with open("six.txt", "r") as f:
        fishes = list(map(int, f.readline().strip("\n").split(",")))
    for fish in fishes:
        curr[0][fish] += 1
    for d in range(1, days+1):
        for i in range(9):
            if i == 8:
                curr[d][8] = curr[d-1][0]
            elif i == 6:
                curr[d][6] = curr[d-1][7] + curr[d-1][0]
            else:
                curr[d][i] = curr[d-1][i+1]
        print("After {} days: {} fishes".format(d, sum(curr[d])))
        
def sum(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum
            
            


if __name__ == "__main__":
    partOne(80)
    partTwo(256)