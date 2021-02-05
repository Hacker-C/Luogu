class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        l = len(nums)
        for i in range(1, l):
            nums[i] += nums[i-1] if nums[i-1] > 0 else 0
            if nums[i] > ans:
                ans = nums[i]
        return ans
