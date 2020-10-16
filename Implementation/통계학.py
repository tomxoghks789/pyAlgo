from collections import Counter
import sys
N = int(sys.stdin.readline())
ans = []
acc = 0
for _ in range(N):
    temp = int(sys.stdin.readline())
    acc += temp
    ans.append(temp)

ans = sorted(ans)
print(round(acc / N))
print(ans[N//2])
cnt = Counter(ans)
if N == 1:
    print(ans[0])
else:
    cnt = cnt.most_common(2)
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
print(ans[N - 1] - ans[0])