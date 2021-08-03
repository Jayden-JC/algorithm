n = int(input())
m = int(input())
x_list = list(map(int, input().split()))
start = 0
end = n
result = 0
while start <= end:
    mid = (start+end) // 2
    if mid >= x_list[0] and mid >= (n-x_list[-1]):   # 양 끝 확인
        breaker = False
        for i in range(len(x_list)-1):   # 가로등과 가로등 사이 확인
            if x_list[i+1] - x_list[i] > 2*mid:
                breaker = True
                break
        if breaker == True:
            start = mid + 1
        else:
            result = mid
            end = mid - 1
    else:
        start = mid + 1
print(result)