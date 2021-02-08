#解法一
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)

#解法二
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x,y:x^y, nums)
