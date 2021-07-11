t = int(input())
coin_tuple = (0.25*100, 0.10*100, 0.05*100, 0.01*100)

for i in range(t):
    coin_dict = {k:0 for k in coin_tuple}   # 동전 딕셔너리 초기화
    c = int(input())   # 거스름돈
    for coin in coin_tuple:
        coin_dict[coin] = int(c // coin)   # 동전 개수
        c = c % coin   # 남은 거스름돈
        if c == 0:   # 남은 거스름돈이 없는 경우
            for coin in coin_tuple:   # 동전 개수 출력
                print(coin_dict[coin], end=' ')
            break