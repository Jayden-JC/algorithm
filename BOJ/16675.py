ml, mr, tl, tr = input().split()
if (ml == 'S' or mr == 'S') and (tl == 'P' and tr == 'P'):
    print('MS')
elif (ml == 'R' or mr == 'R') and (tl == 'S' and tr == 'S'):
    print('MS')
elif (ml == 'P' or mr == 'P') and (tl == 'R' and tr == 'R'):
    print('MS')
elif (tl == 'S' or tr == 'S') and (ml == 'P' and mr == 'P'):
    print('TK')
elif (tl == 'R' or tr == 'R') and (ml == 'S' and mr == 'S'):
    print('TK')
elif (tl == 'P' or tr == 'P') and (ml == 'R' and mr == 'R'):
    print('TK')
else:
    print('?')