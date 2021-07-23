from collections import deque

def bfs(graph, start, visited):
    money = 0
    if graph[start][0] == 'L':   # ���������� �ִ� ���
        if money < graph[start][1]:   # �������� ������ �̸��� ���
            money = graph[start][1]   # �������� �ǵ��� ä���ش�.
    elif graph[start][0] == 'T':   # Ʈ���� �ִ� ���
        if money < graph[start][1]:   # �������� ����� �̸��� ���
            return 'No'   # �� �� ����
        else:
            money -= graph[start][1]
    queue = deque([start])
    visited[start] = True   # �湮 ó��
    while queue:
        v = queue.popleft()
        if v == len(graph):   # n�� ���� �湮�� ���
            return 'Yes'
        for i in graph[v][2]:
            if visited[i] != True:
                if graph[i][0] == 'L':   # ���������� �ִ� ���
                    if money < graph[i][1]:   # �������� ������ �̸��� ���
                        money = graph[i][1]   # �������� �ǵ��� ä���ش�.
                elif graph[i][0] == 'T':   # Ʈ���� �ִ� ���
                    if money < graph[i][1]:   # �������� ����� �̸��� ���
                        continue   # �� �� ����
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
        graph[i].append(info[0])   # ���� ���빰
        graph[i].append(int(info[1]))   # ���������̳� Ʈ���� ���س��� �ݾ�
        graph[i].append(list(map(int, info[2:-1])))   # �ٸ� ������ �� �� �ִ� ���� ��ȣ��
    print(bfs(graph, 1, visited))
    n = int(input())