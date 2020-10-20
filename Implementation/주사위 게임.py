# 2476
import sys
N = int(sys.stdin.readline())
ans = 0
for i in range(N):
    temp = 0
    dice = list(map(int, sys.stdin.readline().split()))
    dice.sort()
    front = dice[0]
    back = dice[1]
    if back > front:
        front = back
    x = dice.count(front)
    if x == 3:
        temp = 10000 + front * 1000
    if x == 2:
        temp = 1000 + front * 100
    if dice[0] != dice[1] != dice[2]:
        temp = max(dice) * 100
    if ans < temp:
        ans = temp
print(ans)