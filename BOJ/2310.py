from collections import deque

def bfs(graph, start, visited):
    money = 0
    if graph[start][0] == 'L':   # 레프리콘이 있는 경우
        if money < graph[start][1]:   # 소지금이 일정량 미만인 경우
            money = graph[start][1]   # 일정량이 되도록 채워준다.
    elif graph[start][0] == 'T':   # 트롤이 있는 경우
        if money < graph[start][1]:   # 소지금이 통행료 미만인 경우
            return 'No'   # 갈 수 없음
        else:
            money -= graph[start][1]
    queue = deque([start])
    visited[start] = True   # 방문 처리
    while queue:
        v = queue.popleft()
        if v == len(graph):   # n번 방을 방문한 경우
            return 'Yes'
        for i in graph[v][2]:
            if visited[i] != True:
                if graph[i][0] == 'L':   # 레프리콘이 있는 경우
                    if money < graph[i][1]:   # 소지금이 일정량 미만인 경우
                        money = graph[i][1]   # 일정량이 되도록 채워준다.
                elif graph[i][0] == 'T':   # 트롤이 있는 경우
                    if money < graph[i][1]:   # 소지금이 통행료 미만인 경우
                        continue   # 갈 수 없음
                    else:
                        money -= graph[i][1]
                queue.append(i)
                visited[i] = True
    return 'No'

n = int(input())
while n != 0:
    graph = {k:[] for k in range(1,n+1)}
    visited = {k:False for k in range(1,n+1)}
    for i in range(1, n+1):
        info = list(input().split())
        graph[i].append(info[0])   # 방의 내용물
        graph[i].append(int(info[1]))   # 레프리콘이나 트롤이 정해놓은 금액
        graph[i].append(list(map(int, info[2:-1])))   # 다른 방으로 갈 수 있는 문의 번호들
    print(bfs(graph, 1, visited))
    n = int(input())