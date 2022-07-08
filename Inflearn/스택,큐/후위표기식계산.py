arr = input()
stack = []
tmp = 0

for x in arr:
    
    if x.isdecimal():
        stack.append(int(x))
        continue
    
    if x == '+':
        b = stack.pop()
        a = stack.pop()
        tmp = a + b
    elif x == '-':
        b = stack.pop()
        a = stack.pop()
        tmp = a - b
    elif x == '*':
        b = stack.pop()
        a = stack.pop()
        tmp = a * b
    elif x == '/':
        b = stack.pop()
        a = stack.pop()
        tmp = a / b
        
    stack.append(tmp)

print(stack.pop())
    
        
        