nums=[0,0,1,1,1,2,2,3,3,4]
l=len(nums)
nums[:l]=sorted(set(nums))
return len(nums)
