# 1541

subtract = []
ans = 0

inputData = input().split("-")

for i in inputData:
    if "+" not in i:
        subtract.append(int(i))
    else:
        subtract.append(sum(list(map(int, i.split("+")))))
ans = subtract[0]
for i in subtract[1:]:
    ans -= i
print(ans)