code = list(str(input()))
leng = len(code)
res = []
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
cnt = 0
# print(len(alphabet))
def DFS(L):
    global res
    global cnt
    if L >=leng:
        # print(res)
        for i in range(len(res)):
            print(alphabet[res[i]-1],end='')
        print()
        cnt += 1
    else:
        if code[L] == '0':
            return
        res.append(int(code[L]))
        DFS(L+1)
        res.pop()
        if L < leng-1 and int(code[L]+code[L+1]) < len(alphabet):
            res.append(int(code[L]+code[L+1]))
            DFS(L+2)
            res.pop()
        
    
DFS(0)
print(cnt)