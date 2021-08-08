n, k = map(int, input().split())
c = {}
if n == 1:
    print(1)
else:
    c[(1,0)] = 1
    c[(1,1)] = 1
    for i in range(2, n):
        c[(i,0)] = 1
        c[(i,i)] = 1
        for j in range(1, i):
            c[(i,j)] = c[(i-1,j-1)]+c[(i-1,j)]
    print(c[(n-1, k-1)])