n = int(input())
a = []

def f(v,a):
    for i in a:
        if v == i[1]:
            return i
    return False

for i in range(n):
    c,no,name = input().split()
    m = [c,no,name] 
    if m[0] == 'D' and f(m[1],a):
        a.remove(f(m[1],a))
    if m[0] == 'I' and f(m[1],a):
        continue
    if m[0] == 'I':
        a.append(m)

# c = -1
# for i in a[:]:
#     c = c + 1
#     v = f(i[1],a[:],c)
#     if i[0] == 'I' and v:
#         a.remove(i)
#     elif i[0] == 'D':
#         if v:
#             print(v)
#         a.remove(i)
        
# print(a)
        
a = sorted(a, key=lambda x: int(x[1]))


k = list(map(int,input().split()))

for i in k:
    print(a[i-1][1], a[i-1][2] )