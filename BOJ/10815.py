n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
check_list = list(map(int, input().split()))
n_list.sort()
for c in check_list:
    start = 0
    end = len(n_list)-1
    breaker = False
    while start <= end:
        mid = (start+end) // 2
        if n_list[mid] == c:
            print(1, end=' ')
            breaker = True
            break
        elif n_list[mid] > c:
            end = mid - 1
        else:
            start = mid + 1
    if breaker == False:
        print(0, end=' ')