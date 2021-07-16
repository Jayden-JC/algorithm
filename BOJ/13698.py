order = input()
loc_dict = {1:'c1', 2:'c2', 3:'c3', 4:'c4'}   # 컵 네 개 위치('c1' : 작은 공, 'c4' : 큰 공)
for o in order:
    if o == 'A':
        loc_dict[1], loc_dict[2] = loc_dict[2], loc_dict[1]
    elif o == 'B':
        loc_dict[1], loc_dict[3] = loc_dict[3], loc_dict[1]
    elif o == 'C':
        loc_dict[1], loc_dict[4] = loc_dict[4], loc_dict[1]
    elif o == 'D':
        loc_dict[2], loc_dict[3] = loc_dict[3], loc_dict[2]
    elif o == 'E':
        loc_dict[2], loc_dict[4] = loc_dict[4], loc_dict[2]
    else:
        loc_dict[3], loc_dict[4] = loc_dict[4], loc_dict[3]

for k,v in loc_dict.items():
    if v == 'c1':
        print(k)
        
for k,v in loc_dict.items():
    if v == 'c4':
        print(k)