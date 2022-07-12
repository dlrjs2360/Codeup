n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int,input().split())))
    
# dirx = [0,1]
# diry = [1,0]
# rdirx = [-1,0]
# rdiry = [0,-1]
dy = [[0] * n for _ in range(n)]


for i in range(n):
    for j in range(n):
        minv = 1e9
        if i == 0 and j == 0:
            dy[i][j] = a[0][0]
        elif i == 0:
            dy[i][j] = dy[i][j-1] + a[i][j]
        elif j == 0:
            dy[i][j] = dy[i-1][j] + a[i][j]
        else:
            dy[i][j] = min(dy[i-1][j],dy[i][j-1]) + a[i][j]

# print('-------------------------------')
# for i in dy:
#     for j in i:
#         print(j,end =' ')
#     print('')
print(dy[n-1][n-1])