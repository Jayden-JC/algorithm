n = int(input())
d = {k:int(1e9) for k in range(0, n+1)}
u = (3, 5)   # 봉지 단위
d[0] = 0

for i in range(len(u)):
    for j in range(u[i], n+1):
        d[j] = min(d[j], d[j-u[i]]+1)
        
if d[n] == int(1e9):
    print(-1)
else:
    print(d[n])