r, c = map(int, input().split())
state = []
for _ in range(r):
    state.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 1
for i in range(r):
    for j in range(c):
        if state[i][j] == 'W':   # 늑대가 있는 경우
            for k in range(4):   # 변을 공유하는 칸(상, 하, 좌, 우) 확인
                 if 0 <= i+dx[k] <= r-1 and 0 <= j+dy[k] <= c-1:   # 변을 공유하는 칸이 목장의 범위 안에 존재하는 경우
                     if state[i+dx[k]][j+dy[k]] == 'S':   # 양이 있는 지 확인
                         result = 0
        elif state[i][j] == '.':   # 비어있는 경우
            state[i][j] = 'D'   # 울타리 설치

if result == 0:
    print(0)
else:
    print(1)
    for i in range(r):
        for j in range(c):
            print(state[i][j], end='')
        print()         