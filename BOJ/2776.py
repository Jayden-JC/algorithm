t = int(input())

for _ in range(t):
    n = int(input())
    n_list = list(map(int, input().split()))
    m = int(input())
    m_list = list(map(int, input().split()))
    
    n_list.sort()
    
    for i in m_list:
        start = 0
        end = len(n_list) - 1
        breaker = False
        while start <= end:
            mid = (start + end) // 2
            if n_list[mid] == i:
                print(1)
                breaker = True
                break
            elif n_list[mid] > i:
                end = mid - 1
            else:
                start = mid + 1
        if breaker == False:
            print(0)