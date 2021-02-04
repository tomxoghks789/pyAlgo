# 2798

N, M = map(int, input().split())
ans = []
dataList = list(map(int, input().split()))
for i in range(len(dataList)):
    for j in range(i + 1, len(dataList)):
        for k in range(j + 1, len(dataList)):
            temp = dataList[i] + dataList[j] + dataList[k]
            if temp <= M:
                ans.append(temp)
if M in ans:
    print(M)
else:
    print(max(ans))
