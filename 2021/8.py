def partOne():
    sum = 0
    with open("8.txt", "r") as f:
        for line in f.readlines():
            l = line.strip("\n").split(" | ")
            output = l[1].split(" ")
            for o in output:
                if len(o) in {2, 3, 4, 7}:
                    sum += 1
    print(sum)

def partTwo():
    res = 0
    map = {}
    with open("eight.txt", "r") as f:
        for line in f.readlines():
            l = line.strip("\n").split(" | ")
            output = l[1].split(" ")
            inp = l[0].split(" ")
            for i in inp:
                if len(i) == 2:
                    map[1] = set(i)
                elif len(i) == 4:
                    map[4] = set(i)
                elif len(i) == 3:
                    map[7] = set(i)
                elif len(i) == 7:
                    map[8] = set(i)
            for i in inp:
                if len(i) == 5:
                    if len(set(i).intersection(map[1])) == 2:
                        map[3] = set(i)
                    elif len(set(i).intersection(map[4])) == 3:
                        map[5] = set(i)
                    elif len(set(i).intersection(map[4])) == 2:
                        map[2] = set(i)
                elif len(i) == 6:
                    if len(set(i).intersection(map[4])) == 4:
                        map[9] = set(i)
                    elif len(set(i).intersection(map[1])) == 2:
                        map[0] = set(i)
                    elif len(set(i).intersection(map[1])) == 1:
                        map[6] = set(i)
            r = ""
            for o in output:
                for key in map:
                    if set(o) == map[key]:
                        r += str(key)
            res += int(r)
        print(res)

if __name__ == "__main__":
    partOne()
    partTwo()