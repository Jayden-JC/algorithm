while True:   # �׽�Ʈ���̽��� ������ �־����� ����
    try:
        a, b, c = map(int, input().split())
    except:   # �׽�Ʈ���̽��� ���̻� �־����� �ʴ� ���
        break
    count = 0
    while True:
        dis_1 = b - a
        dis_2 = c - b
        if dis_1 == 1 and dis_2 == 1:
            print(count)
            break
        if dis_1 <= dis_2:   # a~b������ ������ b~c������ ���ݺ��� �۰ų� ���� ���
            a, b = b, b+1   # a�� b+1�� �̵� ��, ��ǥ ������� ����
        else:
            b, c = b-1, b   # c�� b-1�� �̵�, ��ǥ ������� ����
        count += 1   # ������ Ƚ�� 1 ����