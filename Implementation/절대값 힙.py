# 11286
import sys
import heapq

heap = []
size = 0

for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    if N != 0:
        heapq.heappush(heap, (abs(N), N))
        size += 1
    else:
        if size == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
            size -= 1