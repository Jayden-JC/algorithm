from collections import deque

def bfs(graph, start, visited):
    if visited[start[0]][start[1]] == 1:
        queue = deque([start])
        visited[start[0]][start[1]] = 2
        while queue:
            v = queue.popleft()
            for i in graph[v]:
                if visited[i[0]][i[1]] == 1:
                    queue.append(i)
                    visited[i[0]][i[1]] = 2
        return True
    return False

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    chart = []
    for _ in range(h):
        chart.append(list(map(int, input().split())))
    graph = {}
    for i in range(h):
        for j in range(w):
            if chart[i][j] == 1:   # 땅인 경우
                graph[(i, j)] = []
                for k in range(8):   # 8방향 확인
                    if 0 <= i+dx[k] <= h-1 and 0 <= j+dy[k] <= w-1:
                        graph[(i, j)].append((i+dx[k], j+dy[k]))
    
    result = 0
    for i in range(h):
        for j in range(w):
            if bfs(graph, (i,j), chart) == True:
                result += 1
    print(result)