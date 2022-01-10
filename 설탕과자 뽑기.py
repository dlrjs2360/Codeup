h, w = map(int,input().split(' '))

d=[]                       
for i in range(h+1) :
  d.append([])         
  for j in range(w+1) : 
    d[i].append(0)
    
n = int(input())


for i in range(n):
    l,c,x,y = map(int,input().split(' '))
    if c == 0:
        for a in range(l):
            d[x][y+a] = 1
    if c == 1:
        for a in range(l):
            d[x+a][y] = 1
    
for i in range(1,h+1):
    for j in range(1,w+1):
        print(d[i][j],end = " ")
    print()