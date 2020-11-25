# 1181
from math import gcd
X, Y = map(int, input().split())
print(gcd(X,Y))
print((X * Y) // gcd(X, Y))