n = int(input())
start = 0
end = n
result = 0
while start <= end:
    mid = (start + end) // 2
    if mid*mid >= n:
        result = mid   # ������ �����ϴ� ��� ������Ʈ
        end = mid - 1
    else:
        start = mid + 1
print(result)