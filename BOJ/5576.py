w_list = []
for _ in range(10):
    w_list.append(int(input()))
    
k_list = []
for _ in range(10):
    k_list.append(int(input()))
    
w_list.sort(reverse=True)
k_list.sort(reverse=True)
w_score = sum(w_list[0:3])
k_score = sum(k_list[0:3])

print(w_score, k_score)