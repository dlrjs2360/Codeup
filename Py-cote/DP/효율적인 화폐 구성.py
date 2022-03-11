n,m = map(int,input().split())

a = []
for i in range(n):
    a.append(int(input()))
a.sort(reverse=True)

d = [0] * 1001

# 화폐들로 나눌 수 없으면 -1을 출력한다.
# 최소의 갯수로 화폐를 구성한다.

# for i in a:
    #너무 어렵다..
