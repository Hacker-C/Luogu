score =  [5, 4, 3, 2, 1]

if len(score) == 1:
    return ['Gold Medal']
if  len(score) == 2:
    if score[0] < score[1]:
        return ["Silver Medal", "Gold Medal"]
    return ["Gold Medal", "Silver Medal"]

sort_score = sorted(score, reverse=True)
dct = {} 
dct[sort_score[0]], dct[sort_score[1]], dct[sort_score[2]] =  "Gold Medal", "Silver Medal", "Bronze Medal"
rank = 4
for i in sort_score[3:]:
    dct[i] = str(rank)
    rank += 1
ans = []
for i in score:
    ans.append(dct[i])
print(ans)
