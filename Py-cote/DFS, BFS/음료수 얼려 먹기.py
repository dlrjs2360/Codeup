# 방문처리를 위한 2차원 배열 준비
# 방문한 곳은 1로 바꿔주기
# 방문처리 배열과 실제 배열에서 둘다 0이면 탐색 함수 실행
# 탐색함수 할 때마다 끝날 때 COUNT + 1

n,m = map(int,input().split())

d = [[0] * m for _ in range(n)]

graph = []
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    if x<= -1 or x >=n or y <=-1 or y >=m:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1 , y)
        dfs(x , y-1)
        dfs(x+1 , y)
        dfs(x , y+1)
        return True
    return False

result = 0

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1
            
print(result)