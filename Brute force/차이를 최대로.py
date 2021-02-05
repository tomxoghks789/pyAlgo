# 10819

from itertools import permutations

lengthOfData = int(input())

dataList = list(map(int, input().split()))
ans = 0
for i in permutations(dataList):
    tempVal = 0
    for j in range(lengthOfData - 1):
        tempVal += abs(i[j] - i[j + 1])
    ans = max(ans, tempVal)
print(ans)
