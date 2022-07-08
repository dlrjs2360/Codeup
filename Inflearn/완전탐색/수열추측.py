# 꼭 다시해보기..




# 파이썬 라이브러리 사용
import itertools as it

n,f = map(int,input().split())
b = [1]* n
cnt = 0
for i in range(1,n):
    b[i] = b[i-1] * (n-i)/i
a = list(range(1,n+1))

for tmp in it.permutations(a): # 모든 수열을 만들어준다 
    sum = 0
    for L,x in enumerate(tmp):
        sum += x*b[L]
    if sum == f:
        for i in tmp:
            print(i,end=' ')
        break