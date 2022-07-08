n = int(input())

def DFS(x):
    if x == n+1:
        for i,v in enumerate(ch):
            if v == 1:
                print(i, end=" ")
        print()
    else :
        ch[x] = 1
        DFS(x+1)
        ch[x] = 0
        DFS(x+1)
ch = [0] * (n+1)
DFS(1)