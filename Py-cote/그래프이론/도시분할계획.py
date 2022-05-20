n,m = map(int,input().split())

for i in range(m):
    a,b,c = map(int,input().split())
    
# 최소 신장 트리로 푸는데 트리구조 MST는 노드마다 부모노드가 하나이므로 부모노드로 가는 간선을 자르면 두 개의 트리로 분리가 된다.
# 따라서 최소 비용으로 마을을 유지하려면 가장 큰 유지비가 사용되는 간선을 자른다.

fee = 0
parent = [0] * n+1




