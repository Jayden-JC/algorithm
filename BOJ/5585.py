total = int(input())
change = 1000 - total   # 거스름돈
types = (500, 100, 50, 10, 5, 1)
count = 0
for t in types:
    count += int(change // t)   # 종류별로 개수를 더함
    change = change % t   # 거스름돈 업데이트
    if change == 0:   # 거스름돈이 0인 경우
        print(count)
        break