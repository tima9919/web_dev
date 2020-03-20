import math
a = int(input())
fl = False
b = []
for i in range(a):
        b.append(int(input()))
for i in range(1, len(b)):
    if b[i]/math.fabs(b[i])== b[i-1]/math.fabs(b[i-1]):
        fl = True
        break
if fl:
    print('YES')
else:
    print('NO')