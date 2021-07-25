from collections import deque

n, m, v = map(int, input().split())
graph = {k:[] for k in range(1, n+1)}
for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

for k in range(1, n+1):   # 번호가 작은 것을 먼저 방문하기 위해 오름차순으로 정렬
    graph[k].sort()

visited_dfs = {k:False for k in range(1, n+1)}
ord_dfs = []
visited_bfs = {k:False for k in range(1, n+1)}
ord_bfs = []

def dfs(graph, start, visited):
    visited[start] = True
    ord_dfs.append(start)
    for i in graph[start]:
        if visited[i] != True:
            dfs(graph, i, visited)
    
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    ord_bfs.append(start)
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] != True:
                queue.append(i)
                visited[i] = True
                ord_bfs.append(i)
    
dfs(graph, v, visited_dfs)
bfs(graph, v, visited_bfs)

for i in ord_dfs:
    print(i, end=' ')
print()
for i in ord_bfs:
    print(i, end=' ')