t = int(input())
coin_tuple = (0.25*100, 0.10*100, 0.05*100, 0.01*100)

for i in range(t):
    coin_dict = {k:0 for k in coin_tuple}   # ���� ��ųʸ� �ʱ�ȭ
    c = int(input())   # �Ž�����
    for coin in coin_tuple:
        coin_dict[coin] = int(c // coin)   # ���� ����
        c = c % coin   # ���� �Ž�����
        if c == 0:   # ���� �Ž������� ���� ���
            for coin in coin_tuple:   # ���� ���� ���
                print(coin_dict[coin], end=' ')
            break