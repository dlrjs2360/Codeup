n = int(input())

a= []

for i in range(n):
    name, score = input().split()
    a.append([name, int(score)])

a.sort(key = lambda x: x[1])

for i in a:
    print(i[0])

