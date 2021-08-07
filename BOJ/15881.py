n = int(input())
s = input()
i = 0
result = 0
while True:
    if i+4 > n:
        break
    if s[i:i+4] == 'pPAp':
        result += 1
        i += 4
    else:
        i += 1
print(result)