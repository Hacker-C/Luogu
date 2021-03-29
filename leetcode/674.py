class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = [1 for x in nums]
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]: dp[i] = dp[i-1]+1
            else: dp[i] = 1
        return max(dp)
