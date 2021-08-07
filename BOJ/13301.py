n = int(input())
d = {k:[0, 0] for k in range(1, n+1)}
d[1] = [1, 1]
d[2] = [1, 2]
for i in range(3, n+1):
    d[i] = [d[i-1][1], d[i-1][0]+d[i-1][1]]

print((d[n][0]+d[n][1])*2)