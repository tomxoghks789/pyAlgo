# 14888

# +, -, *, //
from itertools import permutations
import copy
import sys
input()
minVal = 1000000000
maxVal = -1000000000
dataList = list(map(int, sys.stdin.readline().split()))
methodList = list(map(int, sys.stdin.readline().split()))
methodStr = ""
methodStr += "+" * methodList[0]
methodStr += "-" * methodList[1]
methodStr += "*" * methodList[2]
methodStr += "/" * methodList[3]

for operation in set(permutations(methodStr, len(methodStr))):
    # 계산 로직
    tempList = copy.deepcopy(dataList)
    calVal = tempList.pop(0)
    for idx, op in enumerate(operation):
        if op == "+":
            calVal += tempList[idx]
        elif op == "-":
            calVal -= tempList[idx]
        elif op == "*":
            calVal *= tempList[idx]
        else:
            if calVal < 0:
                calVal = -(calVal)
                calVal //= tempList[idx]
                calVal = -(calVal)
            else:
                calVal //= tempList[idx]
    maxVal = max(maxVal, calVal)
    minVal = min(minVal, calVal)

print(maxVal)
print(minVal)
