n = int(input())
word = []
for i in range(n):
    word.append(input())

for i in range(n-1):
    ip = input()
    if ip in word:
        word.remove(ip)
    
print(word[0])