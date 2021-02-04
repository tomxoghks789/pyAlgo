# 2309

dataList = []
for _ in range(9):
    dataList.append(int(input()))
dataList.sort()
sumVal = sum(dataList)
for i in range(9):
    for j in range(i + 1, 9):
        if sumVal - dataList[i] - dataList[j] == 100:
            for k in range(9):
                if k != i and k != j:
                    print(dataList[k])
            exit()