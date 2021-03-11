nums1 = [2,4]
nums2 = [1,2,3,4]
ans = []
k = 0
for e in nums1:
    flag = True
    for j in range(len(nums2)):
        if nums2[j] == e:
            k = j
            break
    for e2 in nums2[k+1:]:
        if e2 > 2:
            ans.append(e2)
            flag = False
            break
    if flag:
        ans.append(-1)
print(ans)
