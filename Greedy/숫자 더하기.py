def greedy(arr):
    N = int(arr[0])
    arr.remove(arr[0])
    ansNum  = []

    return min(ansNum)
while True:
    ans = list(map(str, input().split()))
    if ans[0] == 0:
        break
    print(greedy(ans))