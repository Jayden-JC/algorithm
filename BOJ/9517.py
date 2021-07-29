k = int(input())
n = int(input())
answers = []
for i in range(n):
    t, z = input().split()
    answers.append([int(t), z])
remaining_time= 3*60+30

for answer in answers:
    if answer[1] == 'N' or answer[1] == 'P':   # 정답을 맞추지 못한 경우나 문제를 스킵한 경우
        remaining_time -= answer[0]
        if remaining_time <= 0:
            break
    else:   # 정답을 맞춘 경우
        remaining_time -= answer[0]
        if remaining_time <= 0:
            break
        else:
            k = k + 1 if k+1<=8 else 1   # 폭탄을 바로 왼쪽에 있는 플레이어에게 넘겨줌
            
print(k)