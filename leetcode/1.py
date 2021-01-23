#nums,target
nums=[2,7,11,15]
target=9
l=len(nums)
flag=0
for i in range(l):
    for j in range(l):
        if i!=j and nums[i]+nums[j]==target:
            print([i,j])
            flag=1
        if flag:
            break
    if flag:
        break
            
