# 프로그래머스 큰 수 만들기

def solution(number, k):
    ans = [number[0]]
    for i in range(1, len(number)):
        if ans[-1] > number[i]:
            ans.append(number[i])
        else:
            while True:
                if k != 0 and len(ans) != 0 and number[i] > ans[-1]:
                    ans.pop(-1)
                    k -= 1
                else:
                    ans.append(number[i])
                    break
    if k != 0:
        return "".join(ans)[:-k]
    return "".join(ans)

print(solution("4177252841", 4))