k = int(input())
n = int(input())
answers = []
for i in range(n):
    t, z = input().split()
    answers.append([int(t), z])
remaining_time= 3*60+30

for answer in answers:
    if answer[1] == 'N' or answer[1] == 'P':   # ������ ������ ���� ��쳪 ������ ��ŵ�� ���
        remaining_time -= answer[0]
        if remaining_time <= 0:
            break
    else:   # ������ ���� ���
        remaining_time -= answer[0]
        if remaining_time <= 0:
            break
        else:
            k = k + 1 if k+1<=8 else 1   # ��ź�� �ٷ� ���ʿ� �ִ� �÷��̾�� �Ѱ���
            
print(k)