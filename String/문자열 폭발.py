# 9935

import sys

txtVal = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()
lastChar = bomb[-1]
lengthOfBomb = len(bomb)
stack = []
for char in txtVal:
    stack.append(char)
    if char == lastChar and ''.join(stack[-lengthOfBomb:]) == bomb:
        del stack[-lengthOfBomb:]
ans = ''.join(stack)
if ans == "":
    print("FRULA")
else:
    print(ans)