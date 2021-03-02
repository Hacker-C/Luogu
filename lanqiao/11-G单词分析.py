dct = {}
word = input()
for l in word:
    if l in dct.keys():
        dct[l] += 1
    else:
        dct[l] = 1
sorted_list = sorted(dct.items(), key=lambda x:x[1], reverse=True)
print(sorted_list[0][0])
print(sorted_list[0][1])
