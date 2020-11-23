# 1316번
N = int(input())
ans = 0
for i in range(N):
    flag = 1
    inputData = input()
    temp = [inputData[0]]
    for j in range(1, len(inputData)):
        if inputData[j] not in temp:
            temp.append(inputData[j])
        else:
            if inputData[j] != temp[len(temp) - 1]:
                flag = 0
    if flag:
        ans += 1
print(ans)