t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    v = list(map(int, input().split()))
    v_no1 = v[-1]
    s_no1 = x / v_no1   # 부스터를 쓰지 않은 경우 경주를 마친 시간
    v_no2 = sorted(v[:-1], reverse=True)[0]   # 가장 빠른 자동차의 속도
    s_no2 = x / v_no2   # 가장 빠른 자동차가 경주를 마친 시간
    if s_no1 < s_no2:   # 부스터를 쓰지 않고 단독 우승이 가능한 경우
        print(0)
        continue
    elif 1+((x-y)/v_no1) >= s_no2:   # 부스터를 최대치로 사용하고도 단독 우승이 불가능한 경우
        print(-1)
        continue
    else:
        start = 1
        end = y
        result = 0
        while start <= end:
            mid = (start + end) // 2
            if 1+(x-mid)/v_no1 < s_no2:
                result = mid
                end = mid - 1
            else:
                start = mid + 1
        print(result)