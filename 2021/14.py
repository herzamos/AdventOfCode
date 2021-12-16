from collections import defaultdict
import math

def update(start, rules, steps):
    conf = defaultdict(int)
    for i in range(len(start)-1):
        conf[(start[i] + start[i+1])] += 1
    for i in range(steps):
        new_conf = conf.copy()
        for k in conf.keys():
            for r in rules:
                if r[0] == k and conf[k] > 0:
                    new_conf[k[0] + r[1]] += conf[k]
                    new_conf[r[1] + k[1]] += conf[k]
                    new_conf[k] -= conf[k]
        conf = new_conf.copy()
    return conf

#-------------- INPUT --------------------------#
with open("14.txt", "r") as f:
    inp = [x.strip() for x in f.readlines()]
    
divide = inp.index("")
start = inp[:divide][0]
rules = [x.split(" -> ") for x in inp[divide+1:]]

#-------------- PART ONE -----------------------#
res = defaultdict(int)
conf = (update(start, rules, 10))
for k in conf.keys():
    res[k[0]] += conf[k]
    res[k[1]] += conf[k]
ma = res[max(res, key=res.get)]
mi = res[min(res, key=res.get)]
print(math.ceil(ma/2 - mi/2))
#-------------- PART TWO -----------------------#
res = defaultdict(int)
conf = (update(start, rules, 40))
for k in conf.keys():
    res[k[0]] += conf[k]
    res[k[1]] += conf[k]
ma = res[max(res, key=res.get)]
mi = res[min(res, key=res.get)]
print(math.ceil(ma/2 - mi/2))