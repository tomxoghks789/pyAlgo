# 10989
import sys

LIMIT = 10001
data = [0] * LIMIT
dataLen = int(sys.stdin.readline())

for i in range(dataLen):
    data[int(sys.stdin.readline())] += 1
for i in range(LIMIT):
    dataVal = data[i]
    if dataVal != 0:
        for j in range(dataVal):
            print(i)