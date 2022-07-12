# DFS로 풀기
# n, lm = map(int,input().split())
# a = []
# for _ in range(n):
#     a.append(list(map(int,input().split())))

# maxp = -1e9

# def DFS(L,P,w):
#     global maxp
    
#     if L > n-1:
#         return
#     if w > lm:
#         return
#     else:
#         maxp = max(maxp,P)
#         DFS(L+1,P+a[L][1],w+a[L][0])
#         DFS(L,P+a[L][1],w+a[L][0])
#         DFS(L+1,P,w)
    
# DFS(0,0,0)

# print(maxp)

# 동적프로그래밍으로 풀기
n, lm = map(int,input().split())
dy = [0]*(lm+1)
for _ in range(n):
    w,v = map(int,input().split())
    for j in range(w,lm+1):
        dy[j] = max(dy[j],dy[j-w]+v)
print(dy[lm])


