def partOne():
    numbers =  []
    cards = []
    results = []
    currResult = []
    currCard = []
    with open("four.txt", "r") as f:
        i = 0
        for line in f.readlines():
            if i == 0:
                numbers = line.replace("\n", "").split(",")
                numbers = list(map(int, numbers))
            if line.strip() != "" and i >= 2:
                currCard.append(list(map(int, line.replace("\n", "").split())))
                currResult.append([False for x in range(len(line.replace("\n", "").split()))])
            else:
                if i >= 2:
                    cards.append(currCard)
                    results.append(currResult)
                    currResult = []
                    currCard = []
            i += 1
    for n in numbers:
        for k in range(len(cards)):
            for i in range(len(cards[0])):
                for j in range(len(cards[0][0])):
                    if cards[k][i][j] == n:
                        results[k][i][j] = True
                    if hasWinningCol(results[k]) != -1 or hasWinningRow(results[k]) != -1:
                        res = 0
                        for i1 in range(len(cards[k])):
                            for j1 in range(len(cards[k][i1])):
                                if not results[k][i1][j1]:
                                    res += cards[k][i1][j1]
                        res *= cards[k][i][j]
                        print(res)
                        return
                        
def partTwo():
    numbers =  []
    cards = []
    results = []
    currResult = []
    currCard = []
    with open("four.txt", "r") as f:
        i = 0
        for line in f.readlines():
            if i == 0:
                numbers = line.replace("\n", "").split(",")
                numbers = list(map(int, numbers))
            if line.strip() != "" and i >= 2:
                currCard.append(list(map(int, line.replace("\n", "").split())))
                currResult.append([False for x in range(len(line.replace("\n", "").split()))])
            else:
                if i >= 2:
                    cards.append(currCard)
                    results.append(currResult)
                    currResult = []
                    currCard = []
            i += 1
    won = [False for x in range(len(cards))]
    for n in numbers:
        for k in range(len(cards)):
            for i in range(len(cards[0])):
                for j in range(len(cards[0][0])):
                    if cards[k][i][j] == n:
                        results[k][i][j] = True
                    if hasWinningCol(results[k]) != -1 or hasWinningRow(results[k]) != -1:
                        won[k] = True
                    c = won.count(True)
                    if c == len(won):
                        res = 0
                        for i1 in range(len(cards[k])):
                            for j1 in range(len(cards[k][i1])):
                                if not results[k][i1][j1]:
                                    res += cards[k][i1][j1]
                        res *= cards[k][i][j]
                        print(res)
                        return
                            
                            
def hasWinningRow(card):
    for i in range(len(card)):
        win = True
        for j in range(len(card[0])):
            win = win & card[i][j]
        if win == True:
            return i
    return -1

def hasWinningCol(card):
    for i in range(len(card[0])):
        win = True
        for j in range(len(card)):
            win = win & card[j][i]
        if win == True:
            return j
    return -1
            
if __name__ == "__main__":
    partOne()
    partTwo()