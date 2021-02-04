# 1182

from itertools import combinations

N, S = map(int, input().split())
dataList = list(map(int, input().split()))
ans = 0

for i in range(1, len(dataList) + 1):
    tempList = list(combinations(dataList, i))
    for j in range(len(tempList)):
        sumVal = sum(tempList[j])
        if sumVal == S:
            ans += 1

print(ans)