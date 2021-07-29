from collections import deque

def bfs(graph, start, visited, end):
    queue = deque([start])
    d = 1   # 이동횟수(나중에 1을 빼줘야 함)
    visited[start[0]][start[1]] = d
    if visited[end[0]][end[1]] != False:
        return
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i[0]][i[1]] == False:
                queue.append(i)
                visited[i[0]][i[1]] = visited[v[0]][v[1]] + 1
                if visited[end[0]][end[1]] != False:
                    return

t = int(input())

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

for _ in range(t):
    l = int(input())
    sp = tuple(map(int, input().split()))   # 시작점
    ep = tuple(map(int, input().split()))   # 끝점
    graph = {}
    visited = [[False]*l for _ in range(l)]
    for i in range(l):
        for j in range(l):
            graph[(i, j)] = []
            for k in range(8):
                if 0 <= i+dx[k] <= l-1 and 0 <= j+dy[k] <= l-1:
                    graph[(i, j)].append((i+dx[k], j+dy[k]))
    bfs(graph, sp, visited, ep)
    print(visited[ep[0]][ep[1]]-1)
    