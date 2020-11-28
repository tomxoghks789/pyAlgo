# 1417
# G사 5번
N = int(input())
if N == 1:
    print(0)
else:
    votes = []
    for i in range(N):
        votes.append(int(input()))
    pick = votes.pop(0)
    votes = sorted(votes, reverse=True)
    ans = 0
    while True:
        if pick > max(votes):
            break
        votes[0] -= 1
        pick += 1
        votes = sorted(votes, reverse=True)
        ans += 1
    print(ans)