class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        import math
        if n <= 0:
            return False
        l = math.log(n, 4)
        return int(l)==l
