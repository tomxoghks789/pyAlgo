

from itertools import permutations
def solution(card, n):
    answer = -1
    idx = 0
    ans = []
    n = tuple(map(int, str(n)))
    for i in permutations(card):
        print(i)
        ans.append(i)
    ans = sorted(set(ans))

    for i in ans:
        if n == i:
            return idx + 1
        idx += 1
    return -1

card1 = [1, 2, 1, 3]
n1 = 1312
ret1 = solution(card1, n1)

print("solution 함수의 반환 값은", ret1, "입니다.")

card2 = [1, 1, 1, 2]
n2 = 1122
ret2 = solution(card2, n2)

print("solution 함수의 반환 값은", ret2, "입니다.")