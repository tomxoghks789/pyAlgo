# 11931

import sys

LIMIT = 1000001
plusData = [0] * LIMIT
minusData = [0] * LIMIT
dataLen = int(input())

for i in range(dataLen):
    temp = int(sys.stdin.readline())
    if temp < 0:
        minusData[abs(temp)] = 1
    else:
        plusData[temp] = 1
for i in reversed(range(LIMIT)):
    if plusData[i] != 0:
        print(i)
for i in range(LIMIT):
    if minusData[i] != 0:
        print('-' + str(i))