from collections import deque

def bfs(graph, start, visited, end):
    queue = deque([start])
    visited[start] = 1   # 나중에 1 빼줘야 함
    if visited[end] != False:
        return visited[end]-1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = visited[v] + 1
                if visited[end] != False:
                    return visited[end]-1
    return -1

n = int(input())
n_list = list(map(int, input().split()))   # 인덱스 주의
a, b = map(int, input().split())
graph = {}
for i in range(1, n+1):
    graph[i] = []
    k = 1
    while True:   # 오른쪽으로 갈 수 있는 징검다리 확인
        if i + (n_list[i-1] * k) <= n:
            graph[i].append(i + (n_list[i-1] * k))
            k += 1
        else:
            break
    k = -1
    while True:   # 왼쪽으로 갈 수 있는 징검다리 확인
        if i + (n_list[i-1] * k) >= 1:
            graph[i].append(i + (n_list[i-1] * k))
            k -= 1
        else:
            break
visited = {k:False for k in range(1, n+1)}
print(bfs(graph, a, visited, b))