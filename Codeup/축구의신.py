t, d = map(int,input().split())

c = (90-t)

while(True):
    c = c - 5
    
    if 5 < c:
        d += 1
        continue
    
    elif c > 0:
        d += 2
        break
    
    else:
        d += 1
        break
        
print(d)

    