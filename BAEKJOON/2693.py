t = int(input())

arr = [[0] for col in range(t)]

for i in range(t):
    arr[i] = list(map(int,input().split(' ')))

for a in arr:
    a.sort()
    print(a[7])