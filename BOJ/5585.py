total = int(input())
change = 1000 - total   # �Ž�����
types = (500, 100, 50, 10, 5, 1)
count = 0
for t in types:
    count += int(change // t)   # �������� ������ ����
    change = change % t   # �Ž����� ������Ʈ
    if change == 0:   # �Ž������� 0�� ���
        print(count)
        break