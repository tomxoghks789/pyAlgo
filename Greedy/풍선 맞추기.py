# 11509번
import sys

def greedy(H, N):
    LIMIT = 1000001
    count = 0
    arr = [0] * LIMIT

    for i in range(N):
        tempVal = H[i]
        if arr[tempVal + 1] == 0:
            count += 1
        else:
            arr[tempVal + 1] -= 1
        arr[tempVal] += 1
    return count

N = int(sys.stdin.readline())
H = list(map(int, sys.stdin.readline().split()))
print(greedy(H, N))