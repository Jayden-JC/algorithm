n = int(input())
line = input()
num_L = line.count('L')
num_ch = n + 1 - int(num_L//2)   # 컵홀더 개수(자리 개수 + 1 - 커플석 쌍 수)
if num_L == 0 :   # 커플석이 없는 경우
    print(n)
else:   # 커플석이 있는 경우
    print(num_ch)