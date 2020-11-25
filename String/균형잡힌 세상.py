# 4949

import sys
def correctCheck(str):
    tempList = []
    for i in range(len(str)):
        if str[i] == "(" or "[":
            tempList.append("(")
        else:
            if len(tempList) > 0:
                if str[i] == ")":
                    if tempList.pop() != "(":
                        return "no"
                if str[i] == "]":
                    if tempList.pop() != "[":
                        return "NO"
            else:
                return "no"
    if len(tempList) > 0:
        return "no"
    return "yes"


while True:
    print(correctCheck(sys.stdin.readline().strip()))
