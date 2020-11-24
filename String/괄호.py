# 9012
import sys
def correctCheck(str):
    tempList = []
    for i in range(len(str)):
        if str[i] == "(":
            tempList.append("(")
        else:
            if len(tempList) > 0:
                if tempList.pop() != "(":
                    return "NO"
            else:
                return "NO"
    if len(tempList) > 0:
        return "NO"
    return "YES"

N = int(sys.stdin.readline())

for i in range(N):
    print(correctCheck(sys.stdin.readline().strip()))
