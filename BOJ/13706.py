n = int(input())
start = 0
end = n
while start <= end:
    mid = (start + end) // 2
    if mid*mid == n:
        print(mid)
        break
    elif mid*mid > n:
        end = mid - 1
    else:
        start = mid + 1