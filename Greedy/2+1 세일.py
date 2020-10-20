import sys

def greedy(milk):
    ans = milk[0]
    for i in range(1, len(milk)):
        if (i + 1) % 3 == 0:
            continue
        else:
            ans += milk[i]
    return ans

N = int(sys.stdin.readline())
milk = [0]
for _ in range(N):
    milk.append(int(sys.stdin.readline()))
milk.sort(reverse=True)
print(greedy(milk))