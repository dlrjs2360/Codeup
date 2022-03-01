n,m = map(int,input().split())

a = []
for i in range(n):
    a.append(int(input()))
a.sort(reverse=True)
d = [0] * (n)
print("a는 ",a)
#d는 나눈 후 나머지들을 저장?
s = 0
d[0] = m % a[0]

#점화식 : Ax = m % Ax-1
for i in range(1,n):
    
    if d[n-1] == m or d[n-1] != 0:
        print(-1)
        break
    
    if d[0] == 0:
        print("정답: ",m // a[0])
        break
    
    d[i] = d[i-1] % a[i]
    
    s = s + (d[i-1] // a[i])
        
    if d[i] == 0:
        print("정답: ",s)
        break
    
    print(i, s, d)
    
print(d)
