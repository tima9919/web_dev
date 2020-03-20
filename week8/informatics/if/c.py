nnn = int(input())
a=int(input())
k1 = 1
k2 = 2
k3 = 3


n3 = (nnn // 10 ** k1) % 10
n2 = (nnn // 10 ** k2) % 10
n1 = (nnn // 10 ** k3) % 10
n4 = (nnn % 10 ** k1)
if n1 == n4 and n2 == n3 and 1:
    print('YES')
else:
    print('NO')