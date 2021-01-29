class Solution:
    """
    leetcode #35 搜索插入位置
    """
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.append('')
        l=len(nums)
        for i in range(l-1):
            if target<=nums[i]:
                for j in range(l-2, i-1, -1):
                    nums[j+1]=nums[j]
                nums[i]=target
                return i
        return l-1
