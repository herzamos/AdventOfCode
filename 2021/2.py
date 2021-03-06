def partOne():
    h = d = 0
    with open("two.txt", "r") as f:
        for line in f.readlines():
            dir = line.rstrip("\n").split()[0]
            x = int(line.split()[1])
            match dir:
                case "forward":
                    h += x
                case "up":
                    d -= x
                case "down":
                    d += x
    print(h*d)

def partTwo():
    h = d = a = 0
    with open("2.txt", "r") as f:
        for line in f.readlines():
            dir = line.rstrip("\n").split()[0]
            x = int(line.split()[1])
            match dir:
                case "forward":
                    h += x
                    d += x * a
                case "up":
                    a -= x
                case "down":
                    a += x
    print(h*d)
    
if __name__ == "__main__":
    partOne()
    partTwo()

                    
                