from collections import deque

n, m = map(int, input().split())
shape = []
for _ in range(n):
    shape.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
    
graph = {}   # 2차원 배열을 그래프로 변경
for i in range(n):
    for j in range(m):
        graph[(i,j)] = []
        if shape[i][j] == '-':   # '-' 모양인 경우
            for k in range(2,4):
                if 0 <= i+dx[k] <= n-1 and 0 <= j+dy[k] <= m-1:   # 같은 행에 인접한 인덱스가 범위 안에 있는 경우
                    if shape[i][j] == shape[i+dx[k]][j+dy[k]]:   # 같은 모양인지 확인
                        graph[(i,j)].append((i+dx[k], j+dy[k]))
        else:   # '|' 모양인 경우
            for k in range(0,2):
                if 0 <= i+dx[k] <= n-1 and 0 <= j+dy[k] <= m-1:   # 같은 열에 인접한 인덱스가 범위 안에 있는 경우
                    if shape[i][j] == shape[i+dx[k]][j+dy[k]]:   # 같은 모양인지 확인
                        graph[(i,j)].append((i+dx[k], j+dy[k]))

def bfs(graph, start, visited):
    if visited[start[0]][start[1]] != True:   # 방문한 적이 없는 경우
        queue = deque([start])
        visited[start[0]][start[1]] = True   # 방문 처리
        while queue:
            v = queue.popleft()
            for i in graph[v]:
                if visited[i[0]][i[1]] != True:
                    queue.append(i)
                    visited[i[0]][i[1]] = True   # 같은 나무 판자 방문 처리
        return True
    return False   # 이미 방문한 경우

result = 0
for i in range(n):
    for j in range(m):
        if bfs(graph, (i,j), shape) == True:   # 방문한 것이 없는 경우 같은 나무 판자 모두 방문 처리
            result += 1
            
print(result)