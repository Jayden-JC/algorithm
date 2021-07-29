n = int(input())
candidate_dict = {1:{'score':0, 1:0, 2:0, 3:0}, 2:{'score':0, 1:0, 2:0, 3:0}, 3:{'score':0, 1:0, 2:0, 3:0}}
for _ in range(n):
    s1, s2, s3 = map(int, input().split())
    candidate_dict[1]['score'] += s1
    candidate_dict[1][s1] += 1
    candidate_dict[2]['score'] += s2
    candidate_dict[2][s2] += 1
    candidate_dict[3]['score'] += s3
    candidate_dict[3][s3] += 1

candidate_list = [[i, candidate_dict[i]['score'], candidate_dict[i][3], candidate_dict[i][2], candidate_dict[i][1]] for i in range(1, 4)]

candidate_list.sort(key=lambda x : x[3], reverse=True)   # 2점 개수로 내림차순 정렬
candidate_list.sort(key=lambda x : x[2], reverse=True)   # 3점 개수로 내림차순 정렬
candidate_list.sort(key=lambda x : x[1], reverse=True)   # 총점으로 내림차순 정렬

if candidate_list[0][1] == candidate_list[1][1] and candidate_list[0][2] == candidate_list[1][2] and candidate_list[0][3] == candidate_list[1][3]:   # 총점, 3점 개수, 2점 개수가 모두 같은 경우
    print(0, candidate_list[0][1])
else:
    print(candidate_list[0][0], candidate_list[0][1])