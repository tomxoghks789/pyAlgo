# 15688

import sys

LIMIT = 1000001
data = [0] * LIMIT
dataLen = int(input())
for i in range(dataLen):
    data[abs(int(sys.stdin.readline()))] += 1
for i in range(LIMIT):
    dataVal = data[i]
    if dataVal != 0:
        for j in range(dataVal):
            print(i)