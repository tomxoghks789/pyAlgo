# 1475번

N = input()
arr = [0] * 10
ans = 0
t1, t2 = divmod(N.count('6') + N.count('9'), 2)
N =N.replace('6', '')
N =N.replace('9', '')
ans = t1 + t2
for i in range(len(N)):
    arr[int(N[i])] += 1
if ans > max(arr):
    print(ans)
else:
    print(max(arr))