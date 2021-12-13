def partOne():
    with open("3.txt", "r") as f:
        i = 0
        gamma = epsilon = ""
        b = []
        
        for line in f.readlines():
            if i == 0:
                for char in line.strip("\n"):
                    b.append(1 if char == "1" else -1)
            else:
                for i in range(len(line.strip("\n"))):
                    b[i] += 1 if line[i] == "1" else -1
            i += 1
        for i in range(len(b)):
            mcb = 1 if b[i] > 0 else 0
            lcb = 1 if b[i] < 0 else 0
            gamma += str(mcb)
            epsilon += str(lcb)
        print(int(gamma, 2) * int(epsilon, 2))
        
def partTwo():
    oxygen = []
    co2 = []
    oxygenFound = co2Found = False
    with open("three.txt", "r") as f:
        for line in f.readlines():
            oxygen.append(line.strip("\n"))
            co2.append(line.strip("\n"))
        l = len(oxygen[0])
        for i in range(l):
            if not oxygenFound:
                c = 0
                for line in oxygen:
                    c += 1 if int(line[i]) == 1 else -1
                mcb = 1 if c >= 0 else 0
                oxygen = [x for x in oxygen if int(x[i]) == mcb]
                if len(oxygen) == 1:
                    oxygenFound = True
            if not co2Found:
                c = 0
                for line in co2:
                    c += 1 if int(line[i]) == 1 else -1
                lcb = 0 if c >= 0 else 1
                co2 = [x for x in co2 if int(x[i]) == lcb]
                if len(co2) == 1: 
                    co2Found = True        
        print(int(oxygen[0], 2) * int(co2[0], 2))
            

if __name__ == "__main__":
    partOne()
    partTwo()