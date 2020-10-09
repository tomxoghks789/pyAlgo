def greedy(arr):
    N = int(arr[0])
    arr.remove(arr[0])
    ansNum  = []
    for i in range(N - 1):
        for j in range(i + 1, N):

            ansNum.append(2)
    return min(ansNum)
while True:
    ans = list(map(str, input().split()))
    if ans[0] == 0:
        break
    print(greedy(ans))