a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

result = 0
if a < 0:   # ��Ⱑ 0���� �̸��� ���
    result = (0-a)*c + d + (b-0)*e   # ����ִ� ��⸦ ����� �� �ɸ��� �ð� + ����ִ� ��⸦ �ص��ϴ� �� �ɸ��� �ð� + ������� ���� ��⸦ ����� �� �ɸ��� �ð�
elif a > 0:   # ��Ⱑ 0���� �ʰ��� ���
    result = (b-a)*e
    
print(result)