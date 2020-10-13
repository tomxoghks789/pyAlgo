# 11399번
N = int(input())
P = sorted(list(map(int, input().split())))
ans = 0
for i in range(N):
    ans += sum(P[:i+1])
print(ans)