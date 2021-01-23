# 1744

import sys

ans = 0
positiveVal = []
negativeVal = []

for i in range(int(input())):
    temp = int(sys.stdin.readline())
    if temp == 1:
        ans += 1
        continue
    if temp <= 0:
        negativeVal.append(temp)
    else:
        positiveVal.append(temp)

positiveVal.sort(reverse=True)
negativeVal.sort()

posiLen = len(positiveVal)
negaLen = len(negativeVal)

for i in range(0, posiLen, 2):
    if i + 1 < posiLen:
        ans += positiveVal[i] * positiveVal[i + 1]
    else:
        ans += positiveVal[i]

for i in range(0, negaLen, 2):
    if i + 1 < negaLen:
        ans += negativeVal[i] * negativeVal[i + 1]
    else:
        ans += negativeVal[i]
print(ans)