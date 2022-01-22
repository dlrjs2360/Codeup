n = input()

a = int(n[0]) * 2
b = n[1]
c = int(b) * 2
if c >= 10:
    c = c % 10

d = c * 10 + a

print(d)
if d <= 50:
    print('GOOD')
else :
    print('OH MY GOD')