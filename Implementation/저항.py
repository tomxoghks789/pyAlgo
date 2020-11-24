# 1076
import sys
color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

ans = ""
for i in range(2):
    ans = ans + str(color.index(sys.stdin.readline().strip()))

print(int(ans) * (10 ** color.index(sys.stdin.readline().strip())))