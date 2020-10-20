# 1946
import sys

def greedy(sd, N):
    ans = 1
    current = sd[1]
    for i in range(2, N +1):
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
    print(greedy(scoreData, N))