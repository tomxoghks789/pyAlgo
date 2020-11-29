# 10101

data = []
for i in range(3):
    data.append(int(input()))

if data.count(60) == 3:
    print("Equilateral")
if sum(data) == 180:
    if data.count(data[0]) == 2 or data.count(data[1]) == 2:
        print("Isosceles")
    if data.count(data[0]) == 1 and data.count(data[1]) == 1:
        print("Scalene")
else:
    print("Error")