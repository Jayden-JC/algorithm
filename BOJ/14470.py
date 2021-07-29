a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

result = 0
if a < 0:   # 고기가 0도씨 미만인 경우
    result = (0-a)*c + d + (b-0)*e   # 얼어있는 고기를 데우는 데 걸리는 시간 + 얼어있는 고기를 해동하는 데 걸리는 시간 + 얼어있지 않은 고기를 데우는 데 걸리는 시간
elif a > 0:   # 고기가 0도씨 초과인 경우
    result = (b-a)*e
    
print(result)