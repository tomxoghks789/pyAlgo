# 14241
import sys

def greedy(slime, N):
    ans = 0
    for i in range(N - 1):
        x = slime[i]
        y = slime[i + 1]
        ans += x * y
        slime[i + 1] = x + y
    return ans

N = int(sys.stdin.readline())

slime = list(map(int, sys.stdin.readline().split()))

print(greedy(slime, N))