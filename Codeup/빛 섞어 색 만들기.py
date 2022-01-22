
r,g,b = map(int,input().split(' '))
c = 0
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i,j,k)
            c+=1;
print(c)