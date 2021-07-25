from collections import deque

t = int(input())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(graph, start, visited):
    if visited[start[0]][start[1]] != 0:   # 방문 처리되지 않은 경우
        queue = deque([start])
        visited[start[0]][start[1]] = 0
        while queue:
            v = queue.popleft()
            for i in graph[v]:
                if visited[i[0]][i[1]] != 0:
                    queue.append(i)
                    visited[i[0]][i[1]] = 0
        return True
    return False
    
for _ in range(t):
    m, n, k = map(int, input().split())
    loc = [[0]*m for _ in range(n)]   # 배추의 위치
    for _ in range(k):
        x, y = map(int, input().split())
        loc[y][x] = 1
    graph = {}
    for i in range(n):
        for j in range(m):
            if loc[i][j] == True:
                graph[(i,j)] = []
                for d in range(4):
                    if 0 <= i+dy[d] <= n-1 and 0 <= j+dx[d] <= m-1:
                        if loc[i+dy[d]][j+dx[d]] == True:
                            graph[(i,j)].append((i+dy[d],j+dx[d]))
    result = 0
    for i in range(n):
        for j in range(m):
            if bfs(graph, (i,j), loc) == True:
                result += 1
    print(result)