# 1316번
import sys
N = int(sys.stdin.readline())
ans = 0
for i in range(N):
    flag = 1
    inputData = sys.stdin.readline()
    temp = [inputData[0]]
    for j in range(1, len(inputData)):
        if inputData[j] not in temp:
            temp.append(inputData[j])
        else:
            if inputData[j] != temp[- 1]:
                flag = 0
    if flag:
        ans += 1
print(ans)