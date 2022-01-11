def is_prime(a):
    for i in range(2,a):
        if a % i == 0:
            return False
    else:
        return True
        
n = int(input())

if n == 1:
    print('wrong number')

for i in range(1,n):
    if i != 1:
        if n % i == 0:
            a, b = [i, n//i]
            if is_prime(a) and is_prime(b):
                print(a, b)
                break
    if i == n-1:
        print('wrong number')


