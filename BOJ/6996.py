t = int(input())
for _ in range(t):
    w1, w2 = input().split()
    w1_list = list(w1)
    w2_list = list(w2)
    w1_list.sort()
    w2_list.sort()
    if w1_list == w2_list:
        print('{} & {} are anagrams.'.format(w1, w2))
    else:
        print('{} & {} are NOT anagrams.'.format(w1, w2))