# 1946
import sys

def greedy(sd):
    ans = 0
    current = 100001
    for i in range(1, len(sd)):
        temp = sd[i]
        if temp < current:
            ans += 1
            current = temp
    return ans

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    scoreData = [0] * (N + 1)
    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        scoreData[x] = y
    print(greedy(scoreData))