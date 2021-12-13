def partOneAndTwo():
    ## part one
    opening = "([{<"
    cost = {")": 3, "]": 57, "}": 1197, ">": 25137}
    closing = {"(": 1, "[": 2, "{": 3, "<": 4}
    stack = []
    found = False
    res = 0
    lines = []
    with open("10.txt", "r") as f:
        for line in f.readlines():
            lines.append(list(line.strip("\n")))
    corrupted = [False for x in range(len(lines))]
    for i in range(len(lines)):
        for char in lines[i]:
            if not found:
                if char in opening:
                    stack.append(char)
                else:
                    if char == ")":
                        if stack[-1] != "(":
                            res += cost[char]
                            found = True
                        stack.pop()
                    elif char == "]":
                        if stack[-1] != "[":
                            res += cost[char]
                            found = True
                        stack.pop()
                    elif char == "}":
                        if stack[-1] != "{":
                            res += cost[char]
                            found = True
                        stack.pop()
                    elif char == ">":
                        if stack[-1] != "<":
                            res += cost[char]
                            found = True
                        stack.pop()
        if found:
            corrupted[i] = True
        found = False
        stack = []
    print(res)
    stack = []
    res = 0
    ress = []
    for i in range(len(lines)):
        if not corrupted[i]:
            for char in lines[i]:
                if char in opening:
                    stack.append(char)
                else:
                    stack.pop()
            stack.reverse()
            for el in stack:
                res *= 5
                res += closing[el]
            ress.append(res)
            res = 0
            stack = []
    ress.sort()
    print(ress)
    print(ress[len(ress) // 2])
    
    
    
    
if __name__ == "__main__":
    partOneAndTwo()