# 11656

ans = []
strData = input()
for i in range(len(strData)):
    ans.append(strData[i:])
for i, x in enumerate(sorted(ans)):
    print(x)