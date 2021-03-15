class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        import math as m
        nums = set()
        for i in range(1, int(m.sqrt(num))+1):
            if num % i == 0:
                nums.add(i)
                nums.add(num//i)
        if sum(nums) - num == num:
            return True
        else:
            return False
