# 15688

import sys
import heapq

dataHeap = []
dataLen = int(sys.stdin.readline())

for i in range(dataLen):
    heapq.heappush(dataHeap, int(sys.stdin.readline()))

while dataHeap:
    print(heapq.heappop(dataHeap))