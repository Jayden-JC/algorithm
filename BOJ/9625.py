k = int(input())
d = {k:[0, 0] for k in range(0, k+1)}
d[0] = [1, 0]
for i in range(1, k+1):
    d[i] = [d[i-1][1], d[i-1][1]+d[i-1][0]]
print(d[k][0], d[k][1])