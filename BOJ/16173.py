from collections import deque

n = int(input())
area = []
for _ in range(n):
    area.append(list(map(int, input().split())))

graph = {}
for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:   # 오른쪽 맨 아래 칸
            break
        graph[(i,j)] = []
        if i+area[i][j] <= n-1:   # 오른쪽으로 이동 가능한 경우
            graph[(i,j)].append((i+area[i][j],j))
        if j+area[i][j] <= n-1:   # 아래쪽으로 이동 가능한 경우
            graph[(i,j)].append((i,j+area[i][j]))

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start[0]][start[1]] = 101   # 방문 처리
    while queue:
        v = queue.popleft()
        if v == (n-1,n-1):   # 오른쪽 맨 아래칸
            return 'HaruHaru'
        for i in graph[v]:
            if visited[i[0]][i[1]] != 101:
                queue.append(i)
                visited[i[0]][i[1]] = 101   # 방문 처리
    return 'Hing'

print(bfs(graph, (0,0), area))