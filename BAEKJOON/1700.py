n,k = map(int,input().split())
arr = list(map(int,input().split()))

stack = []
count = 0

for i in arr:
    if len(stack) == 3:
        break
    
    if i not in stack:
        stack.append(i)
        count += 1
        # print(stack)
    
k2 = k - count

for i in arr[k2+1:]:
    if i in stack:
        continue
    else:
        stack.pop()
        stack.append(i)

# arr에서 3개씩 가져와서 비교해야 한다.
