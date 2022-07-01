n = int(input())
m = int(input())

arr = []
for _ in range(m):
    arr.append(list(map(int,input().split())))
    
start, end = map(int,input().split())

temp = 0
distance = [[999] * n for _ in range(n)]
index = 0
# print(start,end)

for i in range(len(distance)):
    distance[i][i] = 0

for i in arr:
    distance[i[0]-1][i[1]-1] = min(distance[i[0]-1][i[1]-1],i[2])