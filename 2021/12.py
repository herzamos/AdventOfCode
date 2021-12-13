neighbours = {}
with open("12.txt", "r") as f:
        for line in f.readlines():
            u, v = line.strip("\n").split("-")
            if u in neighbours.keys():
                neighbours[u] += [v]
            else:
                neighbours[u] = [v]
            if v in neighbours.keys():
                neighbours[v] += [u]
            else:
                neighbours[v] = [u]

def search(cave = "start", visited = set()):
    if cave == "end": return 1
    if cave in visited:
        if cave.islower():
            return 0
    return sum(search(n, visited|{cave}) for n in neighbours[cave])

def search2(twice, cave = "start", visited = set()):
    if cave == "end": return 1
    if cave in visited:
        if cave == "start": return 0
        if cave.islower():
            if twice:
                return 0
            else:
                twice = True
    return sum(search2(twice, n, visited|{cave}) for n in neighbours[cave])
    
print(search())
print(search2(twice = False))