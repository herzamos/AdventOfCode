def inc(x, y, vx, vy):
    x += vx
    y += vy
    if vx > 0:
        vx -= 1
    elif vx < 0:
        vx += 1
    vy -= 1
    return x, y, vx, vy

with open("17.txt", "r") as f:
    line = f.readline()

def hit(x, y, vx, vy):
    maxy = 0
    while True:
        x, y, vx, vy = inc(x, y, vx, vy)
        maxy = max(y, maxy)
        if 269 <= x <= 292 and -68 <= y <= -44:
            return True
        if x > 292 or y < -68:
            return False

## Part one
print(68 * (68 - 1) / 2)
## Part Two
ans = 0
for x in range(295):
    for y in range(-70, 70):
        if hit(0, 0, x, y):
            ans += 1
            
print(ans)
    