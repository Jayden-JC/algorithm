n = int(input())
line = input()
num_L = line.count('L')
num_ch = n + 1 - int(num_L//2)   # ��Ȧ�� ����(�ڸ� ���� + 1 - Ŀ�ü� �� ��)
if num_L == 0 :   # Ŀ�ü��� ���� ���
    print(n)
else:   # Ŀ�ü��� �ִ� ���
    print(num_ch)