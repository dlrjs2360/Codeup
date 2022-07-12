n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int,input().split())))
    
dy = [[0] * n for _ in range(n)]

