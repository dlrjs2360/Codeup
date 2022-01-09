n = int(input())
c = list(map(int, input().split()))

a = []
for i in range(24):
    a.append(0)

for i in c:
    a[i] += 1

for i in range(23):
    print(a[i+1], end=' ')

