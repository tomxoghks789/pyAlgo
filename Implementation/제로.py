# 10773번
N = int(input())
ans = []
for i in range(N):
    temp = int(input())
    if temp == 0 and len(ans) != 0:
        ans.pop()
    else:
        ans.append(temp)
print(sum(ans))