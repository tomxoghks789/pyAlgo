# 1085

x, y, w, h = list(map(int, input().split()))
ans = [x, y, w - x, h - y]
print(min(ans))