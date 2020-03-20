N = int(input())
a = {}
for i in range(N):
    record = input().split()
    a[record[0]] = (float(record[1])+float(record[2])+float(record[3]))/3
print("%.2f" % a[input()])