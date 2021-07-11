t = int(input())
buttons = (5*60, 1*60, 10)

buttons_dict = {k:0 for k in buttons}
breaker = False

for k in buttons:
    buttons_dict[k] = t//k   # 버튼 누른 횟수
    t = t % k   # 남은 시간
    if t == 0:
        breaker = True   # 시간을 정확히 맞춘 경우
        break

if breaker == True:   # 시간을 정확히 맞춘 경우
    for k in buttons:
        print(buttons_dict[k], end=' ')
else:   # 시간을 정확히 맞출수 없는 경우
    print(-1)