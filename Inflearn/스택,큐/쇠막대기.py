ip = list(str(input()))

rz = 0
res = 0
stack = []

for i,v in enumerate(ip):
    
    if v == '(':
        stack.append(v)

    if v == ')' and ip[i-1] == '(':
        stack.pop()
        res += len(stack)
        
    elif v == ')' and stack :
        res += 1
        stack.pop()
        
print(res)

