# 1032
import sys
N = int(sys.stdin.readline())

dataList = []

for i in range(N):
    dataList.append(sys.stdin.readline().strip())

for i in range(len(dataList[0])):
    flag = 0
    temp = dataList[0][i]
    for j in range(1, N):
        if dataList[j][i] != temp:
            print("?", end="")
            flag = 1
            break
    if not flag:
        print(dataList[0][i], end="")