from collections import deque

n, m = map(int, input().split())
graph = {k:[] for k in range(1, n+1)}
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
 
visited = {k:False for k in range(1, n+1)}

def bfs(graph, start, visited):
    if visited[start] != True:
        queue = deque([start])
        visited[start] = True
        while queue:
            v = queue.popleft()
            for i in graph[v]:
                if visited[i] != True:
                    queue.append(i)
                    visited[i] = True
        return True   # 방문 처리를 완료한 경우
    return False   # 이미 방문 처리가 된 경우
    
result = 0
for i in range(1, n+1):
    if bfs(graph, i, visited) == True:   # 방문 처리를 한 경우
        result += 1
        
print(result)