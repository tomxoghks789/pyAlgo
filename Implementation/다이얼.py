# 5622번
Str = input()
numList = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
ans = 0
for i in range(len(Str)):
    for j in range(len(numList)):
        if Str[i] in numList[j]:
            ans += j + 3
            break
print(ans)