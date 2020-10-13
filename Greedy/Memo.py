temp = list(range(1,6))
N = len(temp)
for i in range(N):
    for j in range(N - 1):
        print(temp)
        a = temp[j]
        b = temp[j + 1]
        temp[j] = b
        temp[j + 1] = a