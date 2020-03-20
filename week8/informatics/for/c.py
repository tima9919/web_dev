import math
a = int(input())
b = int(input())
d = math.ceil(math.sqrt(a))
while d**2 <= b:
    print(d**2)
    d += 1