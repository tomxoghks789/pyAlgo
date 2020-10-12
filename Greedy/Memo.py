
def solution(k, score):
    ans = 0
    ansArr = [0] * max(score)
    for i in range(len(score) - 1):
        t1 = score[i]
        t2 = score[i + 1]
        ansArr[t1 - t2] += 1
    if max(ansArr) >= k:
        return len(score) - max(ansArr)
    return ans

k = 3
score = [24,22,20,10,5,3,2,1]

print(solution(k, score))