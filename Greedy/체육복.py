# 프로그래머스 체육복

def solution(n, lost, reserve):
    answer = 0
    nLost = list(set(lost) - set(reserve))
    nReserve = list(set(reserve) - set(lost))
    answer += (n - len(nLost))
    for i in nLost:
        for j in range(len(nReserve)):
            if abs(i - nReserve[j]) == 1:
                answer += 1
                nReserve[j] = -2
                break
    return answer