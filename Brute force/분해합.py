# 2231

val = int(input())
ans = 0

for i in range(1, val +1):
    tempList = list(map(int, str(i)))
    ans = i + sum(tempList)
    if ans == val:
        print(i)
        break
    if i == val:
        print(0)
        break