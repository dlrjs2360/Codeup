
# 재귀함수
n,k = map(int,input().split())
a = list(map(int,input().split()))
m = int(input())

cnt = 0
res = [0] * k
def DFS(L,s):
    global cnt
    if L == k:
        if sum(res) % m == 0:
            # print(res)
            cnt += 1
    else:
        for i in range(s,n):
            res[L] = a[i]
            print(res)
            DFS(L+1,i+1)
            

DFS(0,0)
print(cnt)


# 라이브러리를 사용
# import itertools as it

# n,k = map(int,input().split())
# a = list(map(int,input().split()))
# m = int(input())

# cnt = 0
# for x in it.combinations(a,k):
#     if sum(x) % m == 0:
#         cnt += 1
        
# print(cnt)