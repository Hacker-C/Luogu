class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=len(nums)
        nums[:l]=sorted(set(nums))
        return len(nums)
