# 7568
import sys
N = int(sys.stdin.readline())
dataList = []
for i in range(N):
    dataList.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    count = 1
    for j in range(N):
        if dataList[i][0] < dataList[j][0] and dataList[i][1] < dataList[j][1]:
            count += 1
    print(count, end=" ")
