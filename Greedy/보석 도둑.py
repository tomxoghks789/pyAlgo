# 1202
import sys
import heapq

def greedy(jewel, bagData):
    ans = 0
    pickedJewel = []
    for _ in range(K):
        bagSize = heapq.heappop(bagData)
        while jewel and bagSize >= jewel[0][0]:
            w, v = heapq.heappop(jewel)
            heapq.heappush(pickedJewel, -v)
        if pickedJewel:
            ans -= heapq.heappop(pickedJewel)
        elif not jewel:
            break
    return ans

N, K = map(int, sys.stdin.readline().split())
M= []
Bag= []

for _ in range(N):
    heapq.heappush(M, list(map(int, sys.stdin.readline().split())))

for _ in range(K):
    heapq.heappush(Bag, int(sys.stdin.readline()))

print(greedy(M, Bag))