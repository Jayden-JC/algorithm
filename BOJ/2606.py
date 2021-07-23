from collections import deque

com_num = int(input())
pair_num = int(input())
graph = {k:[] for k in range(1, com_num+1)}
for _ in range(pair_num):
    c1, c2 = map(int, input().split())
    graph[c1].append(c2)
    graph[c2].append(c1)

visited = {k:False for k in range(1, com_num+1)}
    
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] != True:
                queue.append(i)
                visited[i] = True

bfs(graph, 1, visited)

result = 0
for v in visited.values():
    if v == True:
        result += 1
        
print(result-1)   # 1번 컴퓨터 제외