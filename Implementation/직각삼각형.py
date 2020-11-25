# 4153

while True:
    x = list(map(int, input().split()))
    if sum(x) == 0:
        break
    maxNum = max(x)
    x.remove(maxNum)
    if x[0] ** 2 + x[1] ** 2 == maxNum ** 2:
        print("right")
    else:
        print("wrong")