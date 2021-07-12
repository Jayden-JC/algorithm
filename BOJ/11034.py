while True:   # 테스트케이스의 개수가 주어지지 않음
    try:
        a, b, c = map(int, input().split())
    except:   # 테스트케이스가 더이상 주어지지 않는 경우
        break
    count = 0
    while True:
        dis_1 = b - a
        dis_2 = c - b
        if dis_1 == 1 and dis_2 == 1:
            print(count)
            break
        if dis_1 <= dis_2:   # a~b사이의 간격이 b~c사이의 간격보다 작거나 같은 경우
            a, b = b, b+1   # a를 b+1로 이동 후, 좌표 순서대로 정렬
        else:
            b, c = b-1, b   # c를 b-1로 이동, 좌표 순서대로 정렬
        count += 1   # 움직인 횟수 1 증가