n = int(input())
start = 0
end = n
result = 0
while start <= end:
    mid = (start + end) // 2
    if mid*mid >= n:
        result = mid   # 조건을 만족하는 결과 업데이트
        end = mid - 1
    else:
        start = mid + 1
print(result)